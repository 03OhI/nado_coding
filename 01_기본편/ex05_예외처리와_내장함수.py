"""
[기본편 10-2~11-4] 예외 처리와 내장 함수
- raise        : 특정 상황에서 직접 에러를 발생시킨다.
- 사용자 정의 예외 : Exception 을 상속해 상황에 맞는 예외를 만든다.
- finally      : 예외 발생 여부와 관계없이 마지막에 반드시 실행된다(자원 해제).
- enumerate / map / dir : 자주 쓰는 내장 함수.
"""


class BigNumberError(Exception):
    """자릿수를 초과했을 때 발생시킬 사용자 정의 예외"""
    def __init__(self, msg):
        super().__init__(msg)


def divide(num1, num2):
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {}, {}".format(num1, num2))
    return num1 / num2


if __name__ == "__main__":
    cases = [(6, 3), (7, 0), (12, 3), ("a", 2)]

    for a, b in cases:
        print("\n--- 입력 {} / {} ---".format(a, b))
        try:
            print("결과 :", divide(a, b))
        except ZeroDivisionError:
            print("0 으로 나눌 수 없습니다.")
        except BigNumberError as e:
            print("한 자리 숫자만 입력하세요.", e)
        except TypeError:
            print("숫자만 입력할 수 있습니다.")
        finally:
            print("finally : 계산을 종료합니다.")   # 항상 실행

    print("\n=== 내장 함수 ===")
    subjects = ["국어", "영어", "수학"]

    # enumerate : 인덱스와 원소를 튜플로 함께 돌려준다
    for idx, name in enumerate(subjects, 1):
        print(idx, name)

    # map : 여러 데이터를 한 번에 처리 (내부가 C 로 구현되어 빠름)
    scores = list(map(int, ["90", "85", "100"]))
    print("점수 :", scores, "/ 평균 :", sum(scores) / len(scores))

    # dir : 객체가 가진 속성과 메소드 목록
    print("list 의 메소드 일부 :", [m for m in dir(list) if not m.startswith("_")])
