import requests
from bs4 import BeautifulSoup


# --------------------------------------------------------
# [공통 함수] 웹 페이지에 접속해서 HTML(soup 객체)을 만들어주는 함수
# --------------------------------------------------------
def create_soup(url):
    # 실제 브라우저(크롬)를 통해 접속하는 것처럼 'User-Agent' 정보를 헤더에 담기
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    # 지정된 url로 GET 요청을 보내고 응답받음
    res = requests.get(url, headers=headers)
    # 웹페이지 접속에 실패했다면(예: 404 에러) 바로 프로그램을 멈추고 에러냄.
    res.raise_for_status()
    # 가져온 HTML 문서(res.text)를 파이썬이 분석하기 쉽게 'lxml' 파서를 사용해 요리(BeautifulSoup 객체화)해서 반환
    return BeautifulSoup(res.text, "lxml")


# --------------------------------------------------------
# 1. 헤드라인 뉴스 크롤링 (네이버 정치 섹션)
# --------------------------------------------------------
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/section/100"

    # 공통 함수를 호출해서 정치 섹션의 전체 HTML 데이터를 가져옵니다.
    soup = create_soup(url)

    try:
        # [핵심 로직 - 체이닝 기법]
        # 1. soup.find("ul", ...): 클래스가 'sa_list'인 뉴스 목록의 '큰 뼈대(ul)'를 먼저 1개 찾습니다.
        # 2. .find_all("li", ..., limit=3): 그 뼈대 안에서 개별 뉴스 '항목(li)'들을 찾되, 최대 3개(limit=3)까지만 자릅니다.
        news_list = soup.find("ul", attrs={"class": "sa_list"}).find_all("li", attrs={"class": "sa_item"}, limit=3)

        # enumerate를 쓰면 리스트를 반복할 때 순서 번호(index)와 내용(news)을 동시에 뽑아낼 수 있습니다.
        for index, news in enumerate(news_list):
            # 이번엔 전체 HTML(soup)이 아니라, 잘라낸 '개별 뉴스 한 칸(news)' 안에서만 <a> 태그를 찾습니다.
            a_tag = news.find("a", attrs={"class": "sa_text_title"})

            # .get_text()로 태그 사이의 진짜 텍스트(제목)만 뽑고, .strip()으로 양옆 쓸데없는 띄어쓰기를 날립니다.
            title = a_tag.get_text().strip()

            # <a> 태그가 가진 'href' 속성값(클릭 시 이동할 링크 주소)을 가져옵니다.
            link = a_tag["href"]

            # index는 0부터 시작하므로 +1을 해줘서 1, 2, 3번으로 출력되게 만듭니다.
            print(f"{index + 1}. {title}")
            print(f"  (링크 : {link})")

    except AttributeError:
        # 만약 네이버가 사이트 구조를 바꿔서 요소를 찾지 못해 None이 떨어졌을 때,
        # 프로그램이 펑 터지는 것을 막기 위한 안전장치(예외 처리)입니다.
        print("뉴스 구조가 변경되어 찾을 수 없습니다.")

    # 뉴스 섹션이 끝났다는 것을 보기 좋게 구분하기 위해 줄표(-)를 50개 찍어줍니다.
    print("-" * 50)


# --------------------------------------------------------
# 2. IT 뉴스 크롤링 (네이버 IT/과학 섹션)
# --------------------------------------------------------
def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/section/105"
    soup = create_soup(url)

    try:
        # 헤드라인 뉴스와 똑같은 구조(ul -> li)로 3개의 뉴스 아이템을 찾습니다.
        news_list = soup.find("ul", attrs={"class": "sa_list"}).find_all("li", attrs={"class": "sa_item"}, limit=3)

        for index, news in enumerate(news_list):
            a_tag = news.find("a", attrs={"class": "sa_text_title"})

            title = a_tag.get_text().strip()
            link = a_tag["href"]

            print(f"{index + 1}. {title}")
            print(f"  (링크 : {link})")

    except AttributeError:
        print("뉴스 구조가 변경되어 찾을 수 없습니다.")

    print("-" * 50)


# --------------------------------------------------------
# [메인 실행부]
# 이 파이썬 파일이 직접 실행될 때만 아래 함수들을 작동시키라는 의미입니다.
# --------------------------------------------------------
if __name__ == "__main__":
    scrape_headline_news()
    scrape_it_news()