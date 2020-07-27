import requests
from bs4 import BeautifulSoup
raw = requests.get("https://tv.naver.com/r",headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text,'html.parser')
print(raw)

# 컨테이너: div.cds_type
# 제목: dt.title
# 프로그램명: dd.chn
# 재생수: span.hit
# 좋아요수: span.like

container = html.select("div.cds_type")  # 모범답안에 div.cds_info로 하면 안됨
title = container[0].select_one("dt.title")
chn = container[0].select_one("dd.chn")
hit = container[0].select_one("span.hit")
like = container[0].select_one("span.like")
print(title.text.strip())
print(chn.text.strip())
print(hit.text.strip())
print(like.text.strip())

for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")
    print("제목:", title.text.strip())
    print("프로그램:", chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("============================")