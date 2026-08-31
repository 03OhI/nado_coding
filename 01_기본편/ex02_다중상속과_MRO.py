"""
[기본편 9-5] 다중 상속과 다이아몬드 문제, MRO
- 여러 부모가 같은 이름의 메소드를 가지면 어느 것을 쓸지 모호해진다(Diamond Problem).
- 파이썬은 MRO(Method Resolution Order)로 해결한다.
  탐색 순서 : 자식 → 괄호 안 부모의 왼쪽에서 오른쪽 → 최상위 object
"""


class Unit:
    def burn(self):
        print("Unit.burn : 기본 화염 피해")


class Flyable(Unit):
    def burn(self):
        print("Flyable.burn : 공중 유닛 화염 피해")

    def fly(self, name, location):
        print("[{}] {} 방향으로 날아갑니다.".format(name, location))


class AttackUnit(Unit):
    def burn(self):
        print("AttackUnit.burn : 공격 유닛 화염 피해")


class FlyableAttackUnit(AttackUnit, Flyable):
    """AttackUnit 과 Flyable 을 함께 상속 → 다이아몬드 구조"""
    pass


if __name__ == "__main__":
    valkyrie = FlyableAttackUnit()

    # 괄호 안 왼쪽(AttackUnit)이 먼저이므로 AttackUnit.burn 이 호출된다
    valkyrie.burn()
    valkyrie.fly("발키리", "3시")

    print("\n=== MRO 탐색 순서 ===")
    for i, cls in enumerate(FlyableAttackUnit.__mro__, 1):
        print(i, cls.__name__)
