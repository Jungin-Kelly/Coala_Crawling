import requests
from bs4 import BeautifulSoup


# 컨테이너: tr.athing
# 순위: span.rank
# 제목: a.storylink

# articles = html.select("tr.athing")
# rank = articles[0].select_one("span.rank").text
# print(rank)
# title = articles[0].select_one("a.storylink").text
# print(title)
for i in range (1,5):
    print(i,"페이지")
    raw = requests.get("https://news.ycombinator.com/news?p=i", headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')
    articles = html.select("tr.athing")
    for ar in articles:
        rank = ar.select_one("span.rank").text.strip()
        title = ar.select_one("a.storylink").text.strip()
        print(rank,title)
