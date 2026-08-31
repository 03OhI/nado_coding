"""
[활용편5 15] 산점도와 여러 그래프 배치
- scatter : 두 변수의 관계를 점으로 표현. c 와 cmap 으로 세 번째 변수를 색으로 표현
- subplots(2, 2) : 한 화면에 그래프 4개를 배치하고 axs 배열로 접근
"""
import matplotlib.pyplot as plt
from _data import use_korean_font, load_scores

use_korean_font()
df = load_scores()

# ---------- 1) 산점도 ----------
plt.figure(figsize=(6, 5))
plt.title("영어 - 수학 점수 관계")
scatter = plt.scatter(df["영어"], df["수학"],
                      s=100, c=df["학년"], cmap="viridis")
plt.xlabel("영어")
plt.ylabel("수학")
plt.colorbar(scatter, label="학년")     # 색이 무엇을 뜻하는지 컬러바로 표시
plt.tight_layout()
plt.savefig("04_산점도.png", dpi=100)
plt.show()

# ---------- 2) subplots 로 4개 배치 ----------
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("성적 대시보드")

axs[0][0].bar(df["이름"], df["국어"])
axs[0][0].set_title("국어 (막대)")

axs[0][1].plot(df["이름"], df["영어"], marker="o")
axs[0][1].set_title("영어 (선)")

axs[1][0].barh(df["이름"], df["수학"])
axs[1][0].set_title("수학 (가로 막대)")

axs[1][1].scatter(df["국어"], df["수학"])
axs[1][1].set_title("국어 - 수학")
axs[1][1].set_facecolor("whitesmoke")   # 그래프 영역 배경색
axs[1][1].grid(True)                    # 격자로 가독성 향상

plt.tight_layout()
plt.savefig("04_subplots.png", dpi=100)
plt.show()
