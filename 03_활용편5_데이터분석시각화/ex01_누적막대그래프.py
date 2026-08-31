"""
[활용편5 11] 누적 막대 그래프
- plt.bar() 를 연달아 호출하면 같은 자리에 '덧그려져' 겹친다.
- bottom 에 앞선 데이터의 값을 주면 그 높이에서부터 시작해 층층이 쌓인다.
- label + legend 로 범례를, xticks(rotation=) 로 눈금 회전을 처리한다.
"""
import matplotlib.pyplot as plt
from _data import use_korean_font, load_scores

use_korean_font()
df = load_scores()

plt.figure(figsize=(8, 5))

# 1) 국어 점수 막대
plt.bar(df["이름"], df["국어"], label="국어")

# 2) 영어 점수 막대를 국어 점수 높이에서부터 쌓아 올린다
plt.bar(df["이름"], df["영어"], bottom=df["국어"], label="영어")

# 3) 수학까지 한 층 더 (bottom 은 아래 두 층의 합)
plt.bar(df["이름"], df["수학"], bottom=df["국어"] + df["영어"], label="수학")

plt.title("학생별 과목 점수 (누적)")
plt.xticks(rotation=65)     # 이름이 겹치지 않도록 회전
plt.legend()                # label 로 달아 둔 이름표를 범례로 표시
plt.tight_layout()
plt.savefig("01_누적막대그래프.png", dpi=100)
plt.show()
