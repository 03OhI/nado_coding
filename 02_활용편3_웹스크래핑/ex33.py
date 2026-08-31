import requests
from bs4 import BeautifulSoup


def scrape_naver_search_real_estate(query="헬리오시티"):
    # 네이버 통합검색 URL
    url = f"https://search.naver.com/search.naver?where=nexearch&query={query}"

    # 네이버 봇 차단을 막기 위한 헤더
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"요청 중 에러 발생: {e}")
        return

    soup = BeautifulSoup(res.text, "html.parser")

    # 1. 질문자님이 주신 최상위 컨테이너 탐색
    title_area = soup.select_one("div.title_area")

    if not title_area:
        print("검색 결과에서 아파트 정보를 찾을 수 없습니다. 검색어가 정확한지 확인해주세요.")
        return

    # 2. 아파트 이름 추출
    name_tag = title_area.select_one("strong.name a")
    apt_name = name_tag.get_text(strip=True) if name_tag else "이름 없음"

    # 3. 최근 실거래가 추출 (span.item2.price)
    price_tag = title_area.select_one("span.item2.price")
    recent_price = price_tag.get_text(strip=True) if price_tag else "가격 정보 없음"

    # 4. 거래 상세 정보 (날짜, 층, 면적) 추출
    # span.item2가 두 개 있으므로, 리스트로 모두 가져온 뒤 두 번째 요소 선택
    item2_tags = title_area.select("span.item2")
    recent_details = item2_tags[1].get_text(strip=True) if len(item2_tags) > 1 else "상세 정보 없음"

    # 5. 매물 건수 (매매, 전세, 월세) 추출 (span.item_inner)
    listings = []
    for item in title_area.select("span.item_inner"):
        # 내부의 '매매 556건' 형태를 그대로 텍스트로 추출
        listings.append(item.get_text(strip=True))

    listings_str = " / ".join(listings) if listings else "매물 정보 없음"

    # 결과 출력
    print(f"[{apt_name}] 실거래 요약")
    print(f"▶ 가격정보: {recent_price}")
    print(f"▶ 거래상세: {recent_details}")
    print(f"▶ 현재매물: {listings_str}")


if __name__ == "__main__":
    # 다른 아파트를 검색하고 싶다면 파라미터만 변경하면 됩니다.
    scrape_naver_search_real_estate("헬리오시티")
    # scrape_naver_search_real_estate("은마아파트")