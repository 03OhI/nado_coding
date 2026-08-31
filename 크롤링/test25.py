from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 옵션 설정을 위해 추가
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 브라우저 꺼짐 방지 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# options를 적용하여 브라우저 실행
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

wait = WebDriverWait(browser, 10)

# 1. '가는 날' 버튼 클릭
depart_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='가는 날']")))
browser.execute_script("arguments[0].click();", depart_btn)

# 2. 날짜 선택
day_27 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//b[text()='27']")))
browser.execute_script("arguments[0].click();", day_27[0])

day_28 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//b[text()='28']")))
browser.execute_script("arguments[0].click();", day_28[0])