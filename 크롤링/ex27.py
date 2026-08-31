from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

url = "https://tv.naver.com/r"

# 1. 크롬 브라우저를 백그라운드(또는 실제 창)로 엽니다.
driver = webdriver.Chrome()
driver.get(url)
# 2. 자바스크립트가 영상 데이터를 렌더링할 때까지 잠시 기다려줍니다.
time.sleep(3)
# 3. 데이터가 모두 로딩된 상태의 완성된 HTML을 가져옵니다.
html = driver.page_source
# 브라우저 종료
driver.quit()
# 4. 여기서부터는 기존과 동일하게 BeautifulSoup으로 파싱합니다.
soup = BeautifulSoup(html, "lxml")

# 정규표현식(re)을 사용해 'Top100ClipCard_list_item'으로 시작하는 모든 li 태그 검색
clips = soup.find_all("li", class_=re.compile("^Top100ClipCard_list_item"))

print(f"크롤링된 영상 개수: {len(clips)}개")

with open("naver_tv_source.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())