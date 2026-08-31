import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# 대소문자 오류 방지를 위해 tags로 소문자 수정
browser.get('https://www.w3schools.com/TAgs/tryit.asp?filename=tryhtml_option')

# 로딩 대기 (웹페이지가 완전히 뜨기 전에 요소를 찾는 것을 방지)
browser.implicitly_wait(10) # 최대 10초까지 기다림
time.sleep(5)
# iframe 안으로 진입
browser.switch_to.frame("iframeResult")
# 4번째 항목 선택
#elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[4]')
#elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Audi"]')
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Audi")]')
elem.click()
time.sleep(5)
browser.switch_to.default_content()

