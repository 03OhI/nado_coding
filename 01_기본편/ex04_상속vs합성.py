"""
[기본편 9-5] 상속(Is-a) vs 합성(Has-a)
- 상속 : 자식은 부모의 일종이다. 모든 특징을 강제로 물려받는다.
- 합성 : 객체가 다른 객체를 부품으로 '가지고' 있다.
- 합성은 부품만 교체하면 되므로 결합도가 낮고 다중 상속 문제를 원천 차단한다.
"""


# ---------- 부품(합성에 사용할 기능 객체) ----------
class Lifesteal:
    """얼마나 흡혈할지 결정하는 부품"""
    def __init__(self, ratio):
        self.ratio = ratio

    def heal_amount(self, damage):
        return int(damage * self.ratio)


class Regeneration:
    """턴마다 체력을 회복하는 부품 (부품 교체 예시)"""
    def __init__(self, amount):
        self.amount = amount

    def heal_amount(self, damage):
        return self.amount


# ---------- 합성으로 조립한 유닛 ----------
class Vampire:
    def __init__(self, name, hp, damage, heal_part):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.heal_part = heal_part      # ★ 기능을 '가지고' 있다 (Has-a)

    def attack(self, target_name):
        healed = self.heal_part.heal_amount(self.damage)
        self.hp += healed
        print("[{}] {} 공격! (피해 {} / 회복 {} / 현재 체력 {})".format(
            self.name, target_name, self.damage, healed, self.hp))


if __name__ == "__main__":
    # 부품만 갈아 끼우면 동작이 바뀐다 → Vampire 코드는 수정 불필요
    v1 = Vampire("흡혈귀", 100, 20, Lifesteal(0.5))
    v1.attack("적 유닛")

    v2 = Vampire("재생형 흡혈귀", 100, 20, Regeneration(15))
    v2.attack("적 유닛")
