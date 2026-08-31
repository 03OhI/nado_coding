import re

#abcd, book
#ca?e
#여러가지 가능성 존재

p = re.compile("ca.e") #.은 하나의 문자
#^는 문자열 시작을 의미함
#$ 문자열의 끝

def print_match(m):

    #print(m.group()) 매치되지 않으면 에러발생
    if m:
        print(m.group())
    else:
        print("매칭되지않음")
m = p.match("cafeig") #주어진 문자열의 처음부터 일치하는지 확인
print_match(m)