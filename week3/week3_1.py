import requests
from bs4 import BeautifulSoup #bs4 폴더 안에 여러가지 파일이 있는데 그 중 beautiful soup import 하겠다

raw = requests.get("https://tv.naver.com/r/")  #request 안에 있는 get이라는 함수를 사용할거다
print(raw) #response 200 -> 성공적으로 응답했다.
#print(raw.text)  #소스코드로 가져오기 (just 문자열로 인식해서 가져옴)
html = BeautifulSoup(raw.text,'html.parser') #소스코드 가져오기(단순 문자열x, 소스코드로 인식해서 가져옴)
#print(html)
# 파싱 (parsing): 일련의 문자열을 유의미한 단위로 구분

# 1위~3위 컨테이너: div.inner
# # 제목: dt.title
# # 프로그램명: dd.chn
# # 재생수: span.hit
# # 좋아요수: span.like

#1. 컨테이너 수집
container = html.select("div.inner") #파싱된 html에서 div.inner을 골라줘 (일단 컨테이너를 가져옴 -> 여기엔 1~3위 있음)
#print(container[0]) => 리스트로 가져옴

#2. 영상데이터 수집
title = container[0].select_one("dt.title")
chn = container[0].select_one("dd.chn")
hit = container[0].select_one("span.hit")
like = container[0].select_one("span.like")
print(title.text.strip())  # title이 포함하고 있는 자료중에 테그 말고 text로 인식되는 애만 가져옴
print(chn.text.strip())
print(hit.text.strip())
print(like.text.strip())
#select vs select_one => select는 리스트 안에 들어있는게 여러 개일 때 걔네를 다 훑음.
# select_one은 그 리스트 중에서 제일 위에 있는 애만 떼옴

#3. 반복하기
for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")

    print(title.text.strip())  # title이 포함하고 있는 자료중에 테그 말고 text로 인식되는 애만 가져옴
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)


