"""
[활용편5 12] 다중 막대 그래프
- np.arange(N) 으로 데이터 개수만큼의 기준 좌표를 만든다.
- 기준 좌표에서 막대 너비 w 만큼 좌우로 밀어서 나란히 배치한다.
- width 를 지정하지 않으면 막대가 서로 붙어 버린다.
"""
import numpy as np
import matplotlib.pyplot as plt
from _data import use_korean_font, load_scores

use_korean_font()
df = load_scores()

N = df.shape[0]              # (행 개수, 열 개수) 튜플에서 행 개수
index = np.arange(N)         # 0 ~ N-1 기준 좌표
w = 0.25                     # 막대 너비 = 이동 거리

plt.figure(figsize=(9, 5))
plt.title("학생별 성적")

plt.bar(index - w, df["국어"], width=w, label="국어")   # 왼쪽으로 이동
plt.bar(index,     df["영어"], width=w, label="영어")   # 기준 위치
plt.bar(index + w, df["수학"], width=w, label="수학")   # 오른쪽으로 이동

# X축 눈금 위치에 원하는 텍스트를 매핑
plt.xticks(index, df["이름"], rotation=45)
plt.legend(ncol=3)           # 범례를 가로 3칸으로
plt.tight_layout()
plt.savefig("02_다중막대그래프.png", dpi=100)
plt.show()
