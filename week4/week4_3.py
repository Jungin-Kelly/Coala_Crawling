import requests
from bs4 import BeautifulSoup
f= open("navertv.csv", "w")
f.write("제목, 채널명, 조회수, 좋아요\n")
raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text,'html.parser')
container = html.select("div.inner")

# title = container[0].select_one("dt.title")
# chn = container[0].select_one("dd.chn")
# hit = container[0].select_one("span.hit")
# like = container[0].select_one("span.like")
# print(title.text.strip())
# print(chn.text.strip())
# print(hit.text.strip())
# print(like.text.strip())
for cont in container:
    title = cont.select_one("dt.title").text.strip()
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    title = title.replace(",","")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")

    hit = hit.replace("재생 수"," ")
    like = like.replace("좋아요 수"," ")        #함수 체이닝도 ㄱㄴ
    f.write(title + ',' + chn + ',' + hit + ',' + like + "\n") #f.write 앞에서 정제가 돼야함.  +)콤마주의

    # print(title.text.strip())
    # print(chn.text.strip())
    # print(hit.text.strip())
    # print(like.text.strip())
    # print("="*50)
f.close()

#얘 문제가 있음