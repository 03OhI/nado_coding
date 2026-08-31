"""
[활용편5 프로젝트1] 인구 피라미드
- 남성 데이터에 마이너스(-)를 붙이면 막대가 왼쪽 방향으로 그려진다.
- 숫자가 크므로 정수 나눗셈(// 1000)으로 단위를 '천 명'으로 줄여 가독성을 높인다.
- savefig 로 결과 그래프를 파일로 저장한다.

실제 실습에서는 통계청 엑셀 파일을 pd.read_excel 로 읽고
쉼표(,)를 제거한 뒤 남녀 컬럼을 맞춰 주었다. 여기서는 같은 형태의
예제 데이터를 만들어 동일한 로직을 재현한다.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from _data import use_korean_font

use_korean_font()

ages = ["{}대".format(a) for a in range(0, 100, 10)]
male = pd.Series([2_100_000, 2_450_000, 3_300_000, 3_800_000, 4_200_000,
                  3_500_000, 2_400_000, 1_100_000, 300_000, 20_000], index=ages)
female = pd.Series([1_980_000, 2_310_000, 3_150_000, 3_700_000, 4_150_000,
                    3_600_000, 2_700_000, 1_500_000, 600_000, 70_000], index=ages)

plt.figure(figsize=(9, 6))
plt.title("연령대별 인구 피라미드 (단위: 천 명)")

# 남성 : 음수를 붙여 왼쪽으로
plt.barh(ages, -(male // 1000), label="남성")
# 여성 : 그대로 오른쪽으로
plt.barh(ages, female // 1000, label="여성")

# X축 눈금의 음수 표시를 절대값으로 바꿔 준다
ticks = plt.xticks()[0]
plt.xticks(ticks, [str(abs(int(t))) for t in ticks])

plt.legend()
plt.tight_layout()
plt.savefig("05_인구피라미드.png", dpi=150)
plt.show()
