import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve #urllib -> 기본 라이브러리임
import ssl                                                            #line2,3은 사이트에서 접근 오류나는 걸 막음
ssl._create_default_https_context =ssl._create_unverified_context
raw = requests.get("http://movie.naver.com/movie/running/current.nhn#",headers ={"User-Agent":"Mozilla/5.0"})

html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너 dl.lst_dsc
movies = html.select ("dl.lst_dsc")
for m in movies:

    #제목 dt>a
    title = m.select_one("dt>a")  #'.text' 해야지 테그가 안딸려옴.
    url = title.attrs["href"]     #attrs["속성"] -> 그 속성 안에 있는 값(링크)을 알려줘
    #print(url)
    # print("="*50)
    print(title.text)
    each_raw =requests.get("https://movie.naver.com"+url,headers ={"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')
    #print("https://movie.naver.com"+url)
    #https:/movie.naver.com/movie/bi/mi/basic.nhn?code=167605 -> 일반적인 url
    #/movie/bi/mi/basic.nhn?code=167605 ->  href 속성에 있는 링크 값

    #컨테이너 div.score_result>ul>li
    #평점 div.score_result div.star_score em
    #리뷰  div.score_result div.score_reple p

    reviews = each_html.select("div.score_result>ul>li")

    # for r in reviews:
    #     stars = r.select_one("div.score_result div.star_score em").text
    #     reple = r.select_one(" div.score_result div.score_reple p").text
    #
    #     print(stars, reple)

    #포스터 선택자
    poster = each_html.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]
    #print(poster_src)
    urlretrieve(poster_src, "poster/"+title.text[:2]+".png") #poster 폴더 안에 title[:2].png라는 이름으로 저장하겠다