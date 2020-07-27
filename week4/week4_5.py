import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "채널명", "재생수", "좋아요수"])

raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text,'html.parser')
container = html.select(".cds_info")

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
    chn = cont.select_one(".chn").text.strip()
    hit = cont.select_one(".hit").text.strip()
    like = cont.select_one(".like").text.strip()

    title = title.replace(",","")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")

    hit = hit.replace("재생 수"," ")
    like = like.replace("좋아요 수"," ")
    sheet.append([title, chn, hit , like])
    # print(title.text.strip())
    # print(chn.text.strip())
    # print(hit.text.strip())
    # print(like.text.strip())
    # print("="*50)
wb.save("navertv.xlsx")

