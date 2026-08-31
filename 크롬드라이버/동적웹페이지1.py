import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. 브라우저 설정 및 띄우기
browser = webdriver.Chrome()
browser.maximize_window()  # 창을 최대화하여 더 많은 상품이 보이게 설정

# 2. 네이버 쇼핑
# (영상의 구버전 주소 대신 현재 접속 가능한 메인 주소로 수정했습니다)
browser.get('https://danawa.com/?srsltid=AfmBOorUFAJL_qBxUWzn3WIOdQY9L1EMZIkGyqMJxsquvsZ-chVNrB_z')

# 웹페이지가 로딩될 때까지 최대 10초 대기 (안정성 확보)
browser.implicitly_wait(10)

# '무선마우스' 검색어 입력 및 엔터 (최신 By.XPATH 문법 적용)
elem = browser.find_element(By.XPATH, '//*[@id="AKCSearch"]')
elem.send_keys('무선마우스')
elem.send_keys(Keys.ENTER)
# 검색 결과 페이지 로딩 대기
time.sleep(2)

# 동적 페이지(무한 스크롤) 처리 로직
interval = 2  # 2초에 한 번씩 스크롤 내리기
# 현재 화면의 문서 전체 높이를 자바스크립트로 가져와서 prev_height에 저장
prev_height = browser.execute_script('return document.body.scrollHeight')
# 무한 반복문 시작
while True:
    # 스크롤을 화면 가장 아래로 쭈욱 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # 페이지가 로딩되면서 새로운 상품들이 뜰 때까지 대기 (2초)
    time.sleep(interval)
    # 스크롤을 내린 후의 새로운 문서 높이를 가져와서 curr_height에 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    # 직전 높이(prev)와 현재 높이(curr)를 비교
    if curr_height == prev_height:
        # 스크롤을 내렸는데도 높이 변화가 없다면? = 페이지 끝까지 다 내려왔다는 뜻
        print("스크롤 완료! 모든 데이터 로딩 끝.")
        break  # while 반복문을 탈출하여 스크롤 종료
    # 스크롤이 더 내려가서 높이가 달라졌다면, 다음 비교를 위해 현재 높이를 직전 높이에 덮어씌움
    prev_height = curr_height
browser.execute_script('window.scrollTo(0, 0)')
# 스크롤이 끝난 후 5초 대기 후 브라우저 종료 (결과 확인용)
time.sleep(5)
browser.quit()