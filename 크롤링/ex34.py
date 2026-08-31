import requests
from bs4 import BeautifulSoup


# 공통: 웹 페이지의 BeautifulSoup 객체를 반환하는 함수
def create_soup(url):
    # 크롤링 차단을 막기 위해 User-Agent 헤더 추가
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return BeautifulSoup(res.text, "lxml")


# 1. 네이버 서울 날씨 스크래핑
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?query=서울+날씨"
    try:
        soup = create_soup(url)

        # 날씨 요약 (예: 흐림, 어제보다 OO° 높아요)
        summary = soup.find("p", attrs={"class": "summary"}).get_text()

        # 현재 온도
        curr_temp = soup.find("div", attrs={"class": "temperature_text"}).get_text().replace("현재 온도", "").strip()

        # 최저 / 최고 온도
        min_temp = soup.find("span", attrs={"class": "lowest"}).get_text()
        max_temp = soup.find("span", attrs={"class": "highest"}).get_text()

        # 오전 / 오후 강수 확률
        rain_rates = soup.find_all("span", attrs={"class": "weather_left"})
        morning_rain = rain_rates[0].get_text().strip() if len(rain_rates) > 0 else "N/A"
        afternoon_rain = rain_rates[1].get_text().strip() if len(rain_rates) > 1 else "N/A"

        # 미세먼지 / 초미세먼지
        dust_info = soup.find_all("li", attrs={"class": "item_today"})
        pm10 = dust_info[0].get_text().strip() if len(dust_info) > 0 else "N/A"
        pm25 = dust_info[1].get_text().strip() if len(dust_info) > 1 else "N/A"

        # 출력
        print(summary)
        print(f"{curr_temp} ({min_temp} / {max_temp})")
        print(f"오전 {morning_rain} / 오후 {afternoon_rain}")
        print()
        print(f"{pm10}")
        print(f"{pm25}")

    except Exception as e:
        print("날씨 정보를 가져오지 못했습니다. (CSS 선택자 변경 가능성)", e)
    print("-" * 50)


# 2. 헤드라인 뉴스 (네이버 뉴스 홈)
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/section/100"  # 정치 섹션을 헤드라인으로 대체 활용
    try:
        soup = create_soup(url)
        # 뉴스 리스트 찾기
        news_list = soup.find_all("a", attrs={"class": "sa_text_title"}, limit=3)
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            print(f"{index + 1}. {title}")
            print(f"  (링크 : {link})")
    except Exception as e:
        print("헤드라인 뉴스를 가져오지 못했습니다.", e)
    print("-" * 50)


# 3. IT 뉴스 (네이버 IT/과학 섹션)
def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/section/105"
    try:
        soup = create_soup(url)
        news_list = soup.find_all("a", attrs={"class": "sa_text_title"}, limit=3)
        for index, news in enumerate(news_list):
            title = news.get_text().strip()
            link = news["href"]
            print(f"{index + 1}. {title}")
            print(f"  (링크 : {link})")
    except Exception as e:
        print("IT 뉴스를 가져오지 못했습니다.", e)
    print("-" * 50)


# 4. 해커스 오늘의 영어 회화
def scrape_english_conversation():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"

    try:
        # 크롤링 차단 방지용 헤더
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        # 지문을 감싸고 있는 전체 박스(conv_txt) 찾기
        boxes = soup.find_all("div", attrs={"class": "conv_txt"})

        if len(boxes) >= 2:
            # 해커스 웹사이트 구조상 보통 첫 번째 박스가 영어, 두 번째가 한글입니다.
            print("(영어 지문)")
            eng_sentences = boxes[0].find_all("span", attrs={"class": "conv_sub"})
            for sentence in eng_sentences:
                print(sentence.get_text().strip())

            print("\n(한글 지문)")
            kor_sentences = boxes[1].find_all("span", attrs={"class": "conv_sub"})
            for sentence in kor_sentences:
                print(sentence.get_text().strip())
        else:
            print("지문 텍스트 박스를 찾지 못했습니다. 사이트 구조 변경을 확인하세요.")

    except Exception as e:
        print(f"영어 회화 지문을 가져오지 못했습니다. 에러: {e}")

    print("-" * 50)





# 메인 실행부
if __name__ == "__main__":
    scrape_weather()
    scrape_headline_news()
    scrape_it_news()
    scrape_english_conversation()