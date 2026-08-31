import time
from selenium import webdriver

# 스크롤 사이의 대기 시간 설정 (2초)
interval = 2

# 크롬 웹드라이버 객체 생성 및 브라우저 창 최대화
browser = webdriver.Chrome()
browser.maximize_window()

# 스크래핑할 웹 페이지(네이버 TV 탑100)로 이동
url = "https://tv.naver.com/r"
browser.get(url)

# 웹 페이지의 초기 콘텐츠가 모두 렌더링될 때까지 3초 대기
time.sleep(3)

# 현재 브라우저 문서(body)의 총 높이를 가져와서 prev_height에 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 문서의 끝까지 스크롤을 내리기 위한 무한 반복문 시작
while True:
    # 1. 화면의 가장 아래로 스크롤을 내림 (JavaScript 실행)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 2. 스크롤을 내린 후 새로운 콘텐츠가 로딩될 때까지 interval(2초)만큼 대기
    time.sleep(interval)
    # 3. 스크롤을 내린 후의 새로운 문서 높이를 다시 가져와서 curr_height에 저장 (★수정된 부분)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 4. 스크롤을 내리기 전 높이(prev)와 내린 후 높이(curr)가 같다면?
    # -> 더 이상 새로운 콘텐츠가 로딩되지 않아 바닥에 도달했다는 뜻이므로 반복문 탈출
    if curr_height == prev_height:
        print("스크롤 완료!")
        break
    # 5. 아직 바닥이 아니라면, 다음 반복을 위해 현재 높이를 이전 높이 변수에 덮어씌움
    prev_height = curr_height