import requests
from bs4 import BeautifulSoup
import re  # 정규표현식 사용을 위해 추가


def scrape_english_conversation():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        # 정규표현식을 사용하여 id가 'conv_en_t' 또는 'conv_kor_t' 등으로 시작하는 모든 문장 요소 찾기
        sentences = soup.find_all("div", attrs={"id": re.compile("^conv_")})

        print("(영어 지문)")
        # 처음부터 리스트의 절반까지 자르기 (영어)
        for sentence in sentences[:len(sentences) // 2]:
            print(sentence.get_text().strip())

        print("\n(한글 지문)")
        # 리스트의 절반부터 끝까지 자르기 (한글)
        for sentence in sentences[len(sentences) // 2:]:
            print(sentence.get_text().strip())

    except Exception as e:
        print(f"영어 회화 지문을 가져오지 못했습니다. 에러: {e}")

    print("-" * 50)


if __name__ == "__main__":
    scrape_english_conversation()