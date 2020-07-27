import requests
from bs4 import BeautifulSoup

page = 1
for page in range (1,100,10):  #데이터 요청을 반복 (10단위 페이지) / 요청할 데이터는 URL보고 파악하면 됨
    raw = requests.get("https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EC%95%8C%EB%9D%BC&start="+str(page),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    #컨테이너: ul.type01 > li
    #기사제목: a._sp_each_title
    #언론사: span._sp_each_source

    #1. 컨테이너 수집
    articles = html.select("ul.type01 > li")
    print(articles)
    #2. 기사 데이터 수집
    #title = articles[0].select_one("a._sp_each_title").text
    #source = articles[0].select_one("span._sp_each_source").text

    #print(title,source)
    #3. 반복하기
    for ar in articles:   #한 페이지 안에 데이터 수집 반복
          title = ar.select_one("a._sp_each_title").text
          source = ar.select_one("span._sp_each_source").text
          print(title, source)