from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

interval = 2
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 최신 셀레니움 헤드리스 설정 방식
options.add_argument('--window-size=1920,1080')

# 설정한 options를 넣어 단 하나의 브라우저만 생성!
browser = webdriver.Chrome(options=options)

url = "https://tv.naver.com/r"
browser.get(url)
time.sleep(3)

print("스크롤을 시작합니다. 잠시만 기다려주세요...")
url = "https://tv.naver.com/r"
browser.get(url)
time.sleep(3)

print("스크롤을 시작합니다. 잠시만 기다려주세요...")

prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        print("바닥에 도달했습니다! 스크롤 완료.\n")
        break
    prev_height = curr_height
browser.get_screenshot_as_file("screenshot.png")
html = browser.page_source
browser.quit()

soup = BeautifulSoup(html, "lxml")

clips = soup.find_all("li", class_=re.compile("^Top100ClipCard_list_item"))
print(f"크롤링된 영상 개수: {len(clips)}개\n")
print("-" * 30)

# ==========================================
# aria-label 속성에서 제목 추출하기
# ==========================================
# (앞부분의 스크롤 및 BeautifulSoup html 파싱 코드는 동일하게 둡니다)

for clip in clips:
    # 1. 제목이 있는 a 태그 찾기
    link_element = clip.find("a", class_=re.compile("^Top100ClipCard_link"))
    # 2. 채널명이 있는 요소 찾기
    channel_element = clip.find(attrs={"class": re.compile("channel", re.IGNORECASE)})
    if link_element and channel_element:
        raw_title = link_element.get("aria-label")
        channel_name = channel_element.get_text(strip=True)
        keywords = ["스포츠", "KBO", "야구", "축구", "SPOTV"]
        # 제목이나 채널명 텍스트 안에 키워드가 하나라도 포함되어 있다면 출력
        if any(word in raw_title for word in keywords) or any(word in channel_name for word in keywords):
            print(f"[{channel_name}] {raw_title}")