"""
Nadoflix — 코사인 유사도 기반 영화 추천

실행 순서
    1) python build_similarity.py     <- movies.pickle / cosine_sim.pickle 생성 (한 번만)
    2) streamlit run app.py

설치: pip install streamlit tmdbv3api
"""

import os
import pickle

import streamlit as st
from tmdbv3api import Movie, TMDb

# ─────────────────────────────────────────────────────────────
# 설정
# ─────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTER_BASE = "https://image.tmdb.org/t/p/w500"
TOP_K = 10          # 추천 개수
COLS = 5            # 한 줄에 표시할 포스터 수


def load_key(name: str, fallback: str) -> str:
    """.streamlit/secrets.toml 이 있으면 거기서, 없으면 fallback."""
    try:
        return st.secrets[name]
    except Exception:
        return fallback


tmdb = TMDb()
tmdb.api_key = load_key("TMDB_KEY", "여기에_TMDB_키")
tmdb.language = "ko-KR"
movie = Movie()


# ─────────────────────────────────────────────────────────────
# 데이터
# ─────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    """build_similarity.py 가 만들어 둔 pickle 을 읽는다."""
    with open(os.path.join(BASE_DIR, "movies.pickle"), "rb") as f:
        movies = pickle.load(f)
    with open(os.path.join(BASE_DIR, "cosine_sim.pickle"), "rb") as f:
        cosine_sim = pickle.load(f)
    return movies, cosine_sim


@st.cache_data(ttl=3600, show_spinner=False)
def fetch_details(movie_id: int) -> dict:
    """TMDB에서 한글 제목과 포스터 경로를 가져온다. 캐시해서 API 호출을 아낀다."""
    try:
        d = movie.details(movie_id)
        poster = d["poster_path"]
        return {
            "title": d["title"],
            "poster": POSTER_BASE + poster if poster else None,
        }
    except Exception:
        return {"title": None, "poster": None}


# ─────────────────────────────────────────────────────────────
# 추천 (여기가 코사인 유사도를 쓰는 부분)
# ─────────────────────────────────────────────────────────────
def get_recommendations(movies, cosine_sim, title: str, k: int = TOP_K) -> list[dict]:
    # 1) 영화 제목 -> 전체 데이터에서의 index
    idx = movies[movies["title"] == title].index[0]

    # 2) 그 영화 행의 유사도를 (index, 유사도) 쌍으로
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 3) 유사도 내림차순 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 4) 0번은 자기 자신(유사도 1.0)이므로 제외하고 상위 k개
    sim_scores = sim_scores[1 : k + 1]

    recs = []
    for i, score in sim_scores:
        info = fetch_details(int(movies["id"].iloc[i]))
        recs.append(
            {
                "title": info["title"] or movies["title"].iloc[i],  # TMDB 실패 시 원본 제목
                "poster": info["poster"],
                "score": float(score),
            }
        )
    return recs


# ─────────────────────────────────────────────────────────────
# 화면
# ─────────────────────────────────────────────────────────────
st.set_page_config(page_title="Nadoflix", page_icon="🎬", layout="wide")
st.header("🎬 Nadoflix")
st.caption("장르 · 키워드 · 출연진 · 감독을 벡터화한 뒤 코사인 유사도로 비슷한 영화를 찾습니다.")

try:
    movies, cosine_sim = load_data()
except FileNotFoundError:
    st.error(
        "movies.pickle / cosine_sim.pickle 이 없습니다.\n\n"
        "터미널에서 `python build_similarity.py` 를 먼저 실행하세요."
    )
    st.stop()

title = st.selectbox("좋아하는 영화를 고르세요", movies["title"].values)

if st.button("추천받기", type="primary"):
    with st.spinner("비슷한 영화를 찾는 중..."):
        recs = get_recommendations(movies, cosine_sim, title)

    st.subheader(f"'{title}'와(과) 비슷한 영화 {len(recs)}편")

    # 결과가 10개보다 적어도 안전하게 그린다 (원본은 여기서 IndexError 가능)
    for start in range(0, len(recs), COLS):
        for col, rec in zip(st.columns(COLS), recs[start : start + COLS]):
            with col:
                if rec["poster"]:
                    # 최신 Streamlit에서 경고 뜨면 use_container_width -> width="stretch"
                    st.image(rec["poster"], use_container_width=True)
                else:
                    st.markdown(
                        "<div style='aspect-ratio:2/3;display:flex;align-items:center;"
                        "justify-content:center;border:1px dashed #666;border-radius:8px;"
                        "color:#888;font-size:13px;'>포스터 없음</div>",
                        unsafe_allow_html=True,
                    )
                st.markdown(f"**{rec['title']}**")
                st.caption(f"유사도 {rec['score']:.3f}")
