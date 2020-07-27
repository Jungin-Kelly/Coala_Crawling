import requests
from bs4 import BeautifulSoup

raw = requests.get("http://movie.naver.com/movie/running/current.nhn#",headers ={"User-Agent":"Mozilla/5.0"})

html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너:div.list_item
#제목: div.list_item h4
#평점 span.metascore
#감독
#배우