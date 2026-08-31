import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/TAGs/tryit.asp?filename=tryhtml5_input_type_radio')

# 시선을 결과창 iframe 안으로 이동
# (w3schools의 결과창 iframe id는 'iframeResult')
browser.switch_to.frame("iframeResult")

# 최신 문법을 적용하여 요소 찾기
# 이미지처럼 XPATH를 써도 되지만, id가 명확할 때는 By.ID를 쓰는 것이 가장 깔끔하고 빠르다고 한다.
elem = browser.find_element(By.ID, "html")
# elem = browser.find_element(By.XPATH, '//*[@id="male"]')

elem.click()

# 작업이 끝나면 다시 메인 창으로 시선 복귀
#습관을 들이면 좋다고 한다.
browser.switch_to.default_content()
time.sleep(5)
browser.quit()

