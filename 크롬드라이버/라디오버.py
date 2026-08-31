import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# 대소문자 오류 방지를 위해 tags로 소문자 수정
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

# 로딩 대기 (웹페이지가 완전히 뜨기 전에 요소를 찾는 것을 방지)
browser.implicitly_wait(10) # 최대 10초까지 기다려줍니다.

# iframe 안으로 진입
browser.switch_to.frame("iframeResult")
# 요소 찾기
elem = browser.find_element(By.XPATH, '//*[@id="html"]')
# 클릭 로직
if not elem.is_selected():
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")

# 프레임 복귀 및 종료
browser.switch_to.default_content()
time.sleep(5)
browser.quit()