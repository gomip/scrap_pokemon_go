# https://pokemon.gameinfo.io/ko

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
    url="https://pokemon.gameinfo.io/ko",
    headers={"User-Agent": "Mozilla/5.0"}
)

html = urlopen(
    request,
    context=context
).read()

# html 조회
soup = BeautifulSoup(html, "html.parser")
print("soup: ", soup)

# div class="id" 조회 => 도감번호
gen_class_divs = soup.find_all("div", {"class": "gen"})

# for gen_class_div in gen_class_divs:
#     a_tags = gen_class_div.find_all("a")
#     for a_tag in a_tags:
#         print(a_tag["href"])