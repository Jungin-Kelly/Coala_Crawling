import requests
from bs4 import BeautifulSoup
#컨테이너: div.wrap_cont
#제목: div.wrap_tit.mg_tit
#기사요약 :p.f_eb.desc

for i in range (1,5):
    print("<",i,"페이지의 기사>")
    raw = requests.get("https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=i&q=코알라")
    html = BeautifulSoup(raw.text, 'html.parser')
    articles = html.select("div.wrap_cont")
    for ar in articles:
        title = ar.select_one("div.wrap_tit.mg_tit").text.strip()
        abstract = ar.select_one("p.f_eb.desc").text
        print(title)
        print(abstract)
        print("-"*50)
    print("\n\n")
