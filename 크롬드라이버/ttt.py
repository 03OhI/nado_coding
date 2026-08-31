"""숫자 리스트의 평균, 최댓값, 최솟값을 계산하고 막대그래프로 시각화합니다."""

import sys

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"  # 한글 깨짐 방지 (Windows 기본 폰트)
plt.rcParams["axes.unicode_minus"] = False  # 마이너스 기호 깨짐 방지


def get_numbers():
    if len(sys.argv) > 1:
        raw = sys.argv[1:]
    else:
        raw = input("숫자를 쉼표(,)로 구분해 입력하세요: ").split(",")
    return [float(x) for x in raw if x.strip()]


def main():
    numbers = get_numbers()
    if not numbers:
        print("숫자를 하나 이상 입력해야 합니다.")
        return

    average = sum(numbers) / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print(f"평균: {average:.2f}")
    print(f"최댓값: {maximum}")
    print(f"최솟값: {minimum}")

    labels = [str(i + 1) for i in range(len(numbers))]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(labels, numbers, color="#2a78d6", width=0.6)
    ax.axhline(
        average, color="#898781", linestyle="--", linewidth=1,
        label=f"평균: {average:.2f}",
    )

    ax.set_xlabel("항목")
    ax.set_ylabel("값")
    ax.set_title("숫자 리스트 막대그래프")
    ax.legend()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig("bar_chart.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
