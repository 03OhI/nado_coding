import requests
res = requests.get("http://naver.com")
print("응답코드 : ",res.status_code)

if res.status_code == requests.codes.ok:
    print("wjdwkd")
else:
    print("answprk todrla", res.status_code)

res.raise_for_status()
print("웹스크래핑을 시장합")