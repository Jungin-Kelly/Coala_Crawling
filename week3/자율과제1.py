import requests
from bs4 import BeautifulSoup
# 컨테이너 div.lst_thum_wrap li
# 저자   div.lst_thum_wrap li span.writer
# 제목   div.lst_thum_wrap li a strong
for i in range (1,5): #range도 함수 -> 괄호가 꼭 필요함
    print("<",(i-1)*20+1,"위~",i*20,"위>")  #순위를 나타내고 싶음 1~10위/ 11~20위 이런식으로
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page=",str(i),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')
    container = html.select("div.lst_thum_wrap li")
    for j,cont in enumerate(container): #enumerate-> 앞에 따로 숫자 따로 인덱싱해줌
        print(str((i-1)*20+1+j),"위 서적") #여기서 i는 위에 i임 -> 페이지를 나타내기 위함/ j는 아래 for문에서 새로운 순서
        title = cont.select_one("div.lst_thum_wrap li a strong").text
        writer = cont.select_one("div.lst_thum_wrap li span.writer").text
        print("제목:",title)
        print("     ",writer)


