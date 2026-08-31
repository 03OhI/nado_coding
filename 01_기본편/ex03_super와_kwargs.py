"""
[기본편 9-9] super() 와 **kwargs
- 부모 이름을 직접 호출하면 호출 대상이 코드에 고정되어 유연성이 없다.
- super() 는 실행 시점의 MRO 목록에서 '내 클래스 바로 뒤' 클래스를 호출한다.
- **kwargs 로 남은 인자를 상위에 위임하면 부모에 속성이 추가되어도 수정 범위가 줄어든다.
"""


class Unit:
    def __init__(self, name, hp, speed, **kwargs):
        super().__init__(**kwargs)   # 남은 보따리를 다음 MRO 클래스로 전달
        self.name = name
        self.hp = hp
        self.speed = speed
        print("Unit 초기화       :", name, hp, speed)


class Flyable:
    def __init__(self, flying_speed, **kwargs):
        super().__init__(**kwargs)
        self.flying_speed = flying_speed
        print("Flyable 초기화    :", flying_speed)


class AttackUnit(Unit):
    def __init__(self, damage, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage
        print("AttackUnit 초기화 :", damage)


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, **kwargs):
        # 인자를 하나씩 나열하지 않고 통째로 넘긴다
        super().__init__(**kwargs)
        print("FlyableAttackUnit 초기화 완료\n")


if __name__ == "__main__":
    # 각 클래스가 자기 몫만 빼고 나머지를 super() 로 넘겨 준다
    valkyrie = FlyableAttackUnit(
        name="발키리", hp=200, speed=10, damage=6, flying_speed=12
    )
    print("이름 :", valkyrie.name, "/ 공격력 :", valkyrie.damage,
          "/ 비행속도 :", valkyrie.flying_speed)

    print("=== MRO ===")
    print(" -> ".join(c.__name__ for c in FlyableAttackUnit.__mro__))
