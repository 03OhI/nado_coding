"""
build_similarity.py  —  movies.pickle / cosine_sim.pickle 을 만드는 스크립트

한 번만 실행하면 됩니다:
    python build_similarity.py

필요한 파일 (이 스크립트와 같은 폴더에):
    tmdb_5000_movies.csv
    tmdb_5000_credits.csv

만들어지는 파일:
    movies.pickle       -> id, title 두 컬럼짜리 DataFrame
    cosine_sim.pickle   -> (영화수 x 영화수) 코사인 유사도 행렬

설치: pip install pandas scikit-learn numpy
"""

import os
import pickle
from ast import literal_eval

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 스크립트가 있는 폴더 기준으로 경로를 잡는다 (실행 위치와 무관하게 동작)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MOVIES_CSV = os.path.join(BASE_DIR, "tmdb_5000_movies.csv")
CREDITS_CSV = os.path.join(BASE_DIR, "tmdb_5000_credits.csv")

TOP_N_CAST = 3  # 출연진은 상위 3명만 사용


def check_files() -> None:
    missing = [p for p in (MOVIES_CSV, CREDITS_CSV) if not os.path.exists(p)]
    if missing:
        print("아래 파일을 찾을 수 없습니다:")
        for p in missing:
            print("  -", p)
        print("\n현재 폴더에 있는 파일:")
        for f in sorted(os.listdir(BASE_DIR)):
            print("  -", f)
        raise SystemExit(1)


def get_director(crew: list) -> str:
    """crew 리스트에서 job이 Director인 사람 이름을 뽑는다."""
    for person in crew:
        if person.get("job") == "Director":
            return person.get("name", "")
    return ""


def get_names(items: list, limit: int | None = None) -> list[str]:
    """[{'name': ...}, ...] 형태에서 name만 뽑는다."""
    if not isinstance(items, list):
        return []
    names = [i["name"] for i in items if "name" in i]
    return names[:limit] if limit else names


def clean(text: str) -> str:
    """'Christopher Nolan' -> 'christophernolan'
    공백을 없애야 'Chris Evans'와 'Chris Pratt'이 'chris'로 뭉뚱그려지지 않는다."""
    return str(text).lower().replace(" ", "")


def main() -> None:
    check_files()

    print("1) CSV 읽는 중...")
    movies = pd.read_csv(MOVIES_CSV)
    credits = pd.read_csv(CREDITS_CSV)

    # credits 의 movie_id 를 movies 의 id 와 맞춘다.
    # credits 에도 title 컬럼이 있어서 그대로 merge 하면 title_x / title_y 로 갈라진다.
    credits = credits.rename(columns={"movie_id": "id"})
    credits = credits[["id", "cast", "crew"]]
    movies = movies.merge(credits, on="id")
    print(f"   -> 영화 {len(movies)}편")

    print("2) JSON 문자열 컬럼 파싱 중...")
    # CSV에는 "[{\"id\": 28, \"name\": \"Action\"}, ...]" 같은 문자열로 저장돼 있다.
    for col in ("genres", "keywords", "cast", "crew"):
        movies[col] = movies[col].apply(literal_eval)

    print("3) 특성 추출 중 (장르 / 키워드 / 출연진 / 감독)...")
    movies["director"] = movies["crew"].apply(get_director)
    movies["genres"] = movies["genres"].apply(get_names)
    movies["keywords"] = movies["keywords"].apply(get_names)
    movies["cast"] = movies["cast"].apply(lambda x: get_names(x, TOP_N_CAST))

    def make_soup(row) -> str:
        parts = (
            [clean(g) for g in row["genres"]]
            + [clean(k) for k in row["keywords"]]
            + [clean(c) for c in row["cast"]]
            + [clean(row["director"])] * 2  # 감독은 가중치를 주려고 2번 넣는다
        )
        return " ".join(p for p in parts if p)

    movies["soup"] = movies.apply(make_soup, axis=1)

    print("4) 벡터화 + 코사인 유사도 계산 중...")
    count = CountVectorizer(stop_words="english")
    count_matrix = count.fit_transform(movies["soup"])
    print(f"   -> 행렬 크기: {count_matrix.shape}")

    # float32 로 저장하면 파일 크기가 절반이 된다 (추천 순위는 사실상 동일).
    # 튜토리얼과 완전히 똑같이 하려면 .astype(np.float32) 를 지우면 된다.
    cosine_sim = cosine_similarity(count_matrix, count_matrix).astype(np.float32)
    print(f"   -> 유사도 행렬: {cosine_sim.shape}, {cosine_sim.nbytes / 1024 ** 2:.1f} MB")

    print("5) pickle 저장 중...")
    # 인덱스를 0부터 다시 매겨서 cosine_sim 의 행 번호와 일치시킨다 (중요!)
    movies = movies.reset_index(drop=True)
    slim = movies[["id", "title"]]  # 앱에서 실제로 쓰는 컬럼만 남긴다

    with open(os.path.join(BASE_DIR, "movies.pickle"), "wb") as f:
        pickle.dump(slim, f)
    with open(os.path.join(BASE_DIR, "cosine_sim.pickle"), "wb") as f:
        pickle.dump(cosine_sim, f)

    print("\n완료. movies.pickle / cosine_sim.pickle 생성됨.")

    # 간단한 확인: 첫 영화와 비슷한 영화 5편 출력
    idx = 0
    scores = sorted(enumerate(cosine_sim[idx]), key=lambda x: x[1], reverse=True)[1:6]
    print(f"\n확인 — '{slim['title'].iloc[idx]}'와 비슷한 영화:")
    for i, score in scores:
        print(f"  {slim['title'].iloc[i]}  (유사도 {score:.3f})")


if __name__ == "__main__":
    main()
