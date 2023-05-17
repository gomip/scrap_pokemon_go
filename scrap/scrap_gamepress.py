# https://gamepress.gg/pokemongo/pokemon-list

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl

# SSL Context 객체 생성
context = ssl.create_default_context()

# 인증서 검증 비활성화
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# url 호출
request = Request(
    url="https://gamepress.gg/pokemongo/pokemon/50-shadow",
    headers={"User-Agent": "Mozilla/5.0"}
)

html = urlopen(
    request,
    context=context
).read()

# html 조회
soup = BeautifulSoup(html, "html.parser")
print("soup: ", soup)

# tbody 조회
tbody_tag = soup.find("tbody")
tr_tag = tbody_tag.find_all("tr")

tr_count = len(tr_tag)

print("tr_count: ", tr_count)
