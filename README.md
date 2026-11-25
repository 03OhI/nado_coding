# 나도코딩 파이썬 레벨업 실습 코드

국립순천대학교 SW중심대학사업단 **2026년도 파이썬 레벨업 프로그램** 참여 실습 저장소입니다.
유튜브 '나도코딩' 채널의 파이썬 코딩 무료 강의를 수강하며 작성한 코드를 콘텐츠별로 정리했습니다.

| 폴더 | 콘텐츠 | 주요 내용 |
|---|---|---|
| [`01_기본편`](01_기본편) | 파이썬 강의(기본편) | 상속, 다중 상속과 MRO, super와 **kwargs, 상속 vs 합성, 예외 처리와 내장 함수 |
| [`02_활용편3_웹스크래핑`](02_활용편3_웹스크래핑) | 활용편 3 (웹 크롤링·스크래핑) | requests·BeautifulSoup 파싱, 정규표현식, 네이버TV 동적 렌더링 대응, 무한 스크롤, headless, User-Agent 위장, 날씨·뉴스·영어회화 프로젝트 |
| [`03_활용편4_업무자동화`](03_활용편4_업무자동화) | 활용편 4 (업무자동화 RPA) | XPath, Selenium 4.x 브라우저 제어, iframe 전환, radio·checkbox·option 조작, 동적 웹페이지 자동 스크롤 |
| [`04_활용편5_데이터분석시각화`](04_활용편5_데이터분석시각화) | 활용편 5 (데이터 분석 및 시각화) | 누적·다중 막대 그래프, 원 그래프와 도넛, 산점도와 subplots, 인구 피라미드 |
| [`05_활용편6_이미지처리`](05_활용편6_이미지처리) | 활용편 6 (OpenCV 이미지 처리) | 소벨·캐니 에지 검출, 오츠 이진화와 윤곽선, 사각 윤곽선, 카드 검출, MediaPipe 얼굴 검출 + 스티커 합성 |
| [`06_활용편7_머신러닝`](06_활용편7_머신러닝) | 활용편 7 (머신러닝·영화 추천) | 선형/다중/다항 회귀, 로지스틱 회귀, K-Means, TF-IDF 기반 영화 추천, SVD 협업 필터링 |

## 실행 환경

```bash
pip install pandas numpy matplotlib beautifulsoup4 selenium lxml requests
pip install opencv-python mediapipe
pip install scikit-learn scikit-surprise streamlit
```

## 참고

- `06_활용편7_머신러닝/영화추천프로젝트`는 Kaggle의 **TMDB 5000 Movie Dataset**(`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`)이 필요합니다.
  용량 문제로 저장소에는 포함하지 않았으며, `build_similarity.py`를 실행하면 유사도 행렬(`cosine_sim.pickle`)이 생성됩니다.
- `05_활용편6_이미지처리` 예제는 별도 이미지가 없어도 `_sample.py`가 테스트 이미지를 자동 생성합니다.
  `ex05_얼굴인식_스티커.py`는 웹캠과 투명 PNG 스티커(`right_eye.png`, `left_eye.png`)가 필요합니다.

## 라이선스

03OhI가 저작권을 보유한 기여분에는 [GNU Affero General Public License v3.0](LICENSE) (`AGPL-3.0-only`)가 적용됩니다. 강의에서 가져온 예제, 웹페이지 캡처, 외부 이미지와 데이터에는 각 권리자의 이용 조건이 적용됩니다.
