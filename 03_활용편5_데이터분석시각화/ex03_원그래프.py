"""
[활용편5 13~14] 원 그래프 (기본 / 심화)
- autopct        : 조각의 비율을 자동 계산해 표시 ('%' 를 쓰려면 '%%')
- explode        : 조각을 중심에서 얼마나 떨어뜨릴지 (0 이면 붙어 있음)
- counterclock   : False 면 시계 방향으로 그린다
- wedgeprops     : width 를 1보다 작게 주면 도넛, edgecolor/linewidth 로 경계선
"""
import matplotlib.pyplot as plt
from _data import use_korean_font, load_scores

use_korean_font()
df = load_scores()

grp = df.groupby("학교")          # 학교별로 묶어 인원수 집계
values = grp.size()
labels = values.index

# ---------- 1) 기본 원 그래프 ----------
plt.figure(figsize=(5, 5))
plt.title("학교별 학생 비율 (기본)")
plt.pie(values, labels=labels, autopct="%.1f%%",
        explode=[0.05] * len(values), counterclock=False, startangle=90)
plt.savefig("03_원그래프_기본.png", dpi=100)
plt.show()


# ---------- 2) 도넛 + 사용자 정의 autopct ----------
def custom_autopct(pct):
    """비율이 15% 이상일 때만 정수 퍼센트로 표시, 미만이면 숨김"""
    return "{:.0f}%".format(pct) if pct >= 15 else ""


plt.figure(figsize=(5, 5))
plt.title("학교별 학생 비율 (도넛)")
plt.pie(values, labels=labels, autopct=custom_autopct, counterclock=False,
        startangle=90,
        wedgeprops={"width": 0.5, "edgecolor": "w", "linewidth": 2})
plt.savefig("03_원그래프_도넛.png", dpi=100)
plt.show()
