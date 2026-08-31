"""
[기본편 9-4] 상속(inheritance)과 접근 제어자
- 부모 클래스의 속성과 기능을 자식 클래스가 물려받는다.
- 자식이 __init__을 정의하면 부모의 생성자가 오버라이드되므로
  '부모클래스명.__init__(self, ...)' 로 직접 호출해 주어야 한다.
- 파이썬은 private/protected를 문법으로 강제하지 않고 관례(__, _)로 표현한다.
"""


class Unit:
    def __init__(self, name, hp, speed, unit_id):
        self.name = name
        self._hp = hp            # protected : 자식 클래스까지만 접근 권장
        self.speed = speed
        self.__id = unit_id      # private   : 외부/자식 모두 직접 접근 차단

    def get_id(self):
        """__id 는 메소드를 통해서만 읽도록 캡슐화"""
        return self.__id

    def move(self, location):
        print("[{}] {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, unit_id, damage):
        # ★ 자식이 생성자를 정의했으므로 부모 생성자를 직접 호출해야 한다
        Unit.__init__(self, name, hp, speed, unit_id)
        self.damage = damage

    def attack(self, location):
        print("[{}] {} 방향으로 공격합니다. [공격력 {}]".format(self.name, location, self.damage))

    def damaged(self, dmg):
        # _hp 는 protected 이므로 자식 클래스에서는 자유롭게 사용 가능
        self._hp -= dmg
        print("[{}] {} 데미지를 입었습니다. (남은 체력 {})".format(self.name, dmg, self._hp))
        if self._hp <= 0:
            print("[{}] 파괴되었습니다.".format(self.name))


if __name__ == "__main__":
    firebat = AttackUnit("파이어뱃", 50, 16, "U-001", 6)
    firebat.move("1시")
    firebat.attack("1시")
    firebat.damaged(25)

    print("유닛 ID :", firebat.get_id())          # 메소드를 통한 접근 → 정상
    try:
        print(firebat.__id)                        # 직접 접근 시도 → 실패
    except AttributeError as e:
        print("private 속성 직접 접근 실패 :", e)
