import requests
from bs4 import BeautifulSoup
import re  # 정규표현식 사용


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?query=서울+날씨"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        # 1. 날씨 요약 (예: 흐림, 어제보다 OO° 높아요)
        # 클래스명에 'summary'가 포함된 p 태그 찾기
        summary = soup.find("p", attrs={"class": re.compile("summary")}).get_text().strip()

        # 2. 현재 온도
        # 클래스명에 'temperature'가 포함된 div 태그 찾기
        curr_temp_elem = soup.find("div", attrs={"class": re.compile("temperature_text")})
        curr_temp = curr_temp_elem.get_text().replace("현재 온도", "").strip() if curr_temp_elem else "N/A"

        # 3. 최저 / 최고 온도
        # 클래스명이 'lowest' 또는 'highest'로 시작하는 span 태그 찾기
        min_temp_elem = soup.find("span", attrs={"class": re.compile("^lowest")})
        max_temp_elem = soup.find("span", attrs={"class": re.compile("^highest")})

        min_temp = min_temp_elem.get_text().strip() if min_temp_elem else "N/A"
        max_temp = max_temp_elem.get_text().strip() if max_temp_elem else "N/A"

        # 출력
        print(summary)
        print(f"현재 {curr_temp} ({min_temp} / {max_temp})")

    except Exception as e:
        print(f"날씨 정보를 가져오지 못했습니다. 에러: {e}")

    print("-" * 50)


if __name__ == "__main__":
    scrape_weather()