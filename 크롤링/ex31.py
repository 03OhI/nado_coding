from selenium import webdriver
from selenium.webdriver.common.by import By  # 요소를 찾을 때 사용하는 기준(ID, CLASS_NAME 등)을 정의하는 모듈

options = webdriver.ChromeOptions()
# 1. 브라우저 창을 화면에 띄우지 않고 백그라운드에서 실행 (리소스 절약 및 속도 향상)
options.headless = True
# 2. 헤드리스 모드에서 웹페이지 레이아웃이 모바일 뷰 등으로 깨지는 것을 방지하기 위해 기본 해상도 고정
options.add_argument("window-size=1920x1080")
# 3. 🌟 가장 핵심: 실제 사람이 사용하는 일반 브라우저인 것처럼 서버를 속이기 위해 User-Agent 값 위장
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36")
# 위에서 설정한 옵션들을 적용하여 크롬 웹드라이버 객체 생성
browser = webdriver.Chrome(options=options)
# 가상 브라우저의 창 크기를 최대화 (화면에 보이는 요소들을 모두 렌더링하기 위함)

browser.maximize_window()
# 크롤링할 대상 타겟 URL
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)  # 해당 URL로 접속 요청을 보냄
# HTML 문서 내부에서 id 속성값이 "detected_value"인 단일 요소를 찾아 객체로 반환
detected_value = browser.find_element(By.ID, "detected_value")
# 찾은 웹 요소 객체에서 태그를 제외한 '텍스트(문자열)'만 추출하여 터미널에 출력
print(detected_value.text)
# 크롤링 작업이 끝나면 브라우저를 닫고 메모리를 반환 (필수)
browser.quit()