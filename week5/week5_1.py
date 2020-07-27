# 네이버 영화 데이터 수집
import requests
from bs4 import BeautifulSoup

raw = requests.get("http://movie.naver.com/movie/running/current.nhn#",headers ={"User-Agent":"Mozilla/5.0"})

html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너 dl.lst_dsc
movies = html.select ("dl.lst_dsc")
for m in movies:

    #제목 dt>a
    title = m.select_one("dt>a").text  #'.text' 해야지 테그가 안딸려옴.

    #평점 a>span.num
    score = m.select_one("a>span.num").text
    if float(score) < 8.5:
        continue        #위에서 반복문을 쭉 수행하다가 continue를 만나면 오류내지말고 그 뒤 단계를 생략하고
                        #다음으로 넘어감
    genre_all = m.select_one("dl.lst_dsc dl.info_txt1 dd:nth-of-type(1) span.link_txt ") #첫번째 dd안에 있는 장르 뭉탱이
    if "액션" not in genre_all.text:
            continue           #위에 내용까지 합쳐져서 평점 8.5 미만, 장르에 액션이 안 포함된 애는 수집하지 x 결과만 출력

    print("제목:",title)
    print("평점:",score)
    #장르 dl.lst_dsc dl.info_txt1 dd a
    #감독 dl.lst_dsc dl.info_txt1 dd a   -> 얘네 셋은 동일한 라인에 있는 애들이라 구분이 안됨
    #평점 dl.lst_dsc dl.info_txt1 dd a      별도의 처리가 필요함

# select 함수 이용하는 방법
    # info = m.select("dl.lst_dsc dl.info_txt1 dd") #dd까지만 넣는이유: dd까지는 내용이 같고 a테그에서 내용이 달라짐
    #     #                                               #select -> 리스트로 저장하는 함수 => dd에 딸린 애들을 리스트 취급하겠다.
    #     # #장르
    #     # genre = info[0].select("a")   #장르는 dd테그의 첫번째 아래에 있음/ select_one 안하는 이유는 장르가 여러 개 일수도 있어서
    #     # #감독
    #     # director = info[1].select("a") #감독은 dd테그의 두번째
    #     # #배우
    #     # actor = info[2].select("a")    #배우는 dd테그의 세 번째
    #     # for g in genre:
    #     #     print(g.text)
    #     # for d in director:
    #     #     print(d.text)
    #     # for a in actor:
    #     #     print(a.text)
    #     # print("="*50)   -> 얘 실행하다 오류나는 이유: 중간에 배우가 없어서
    #     Q.try, except 사용하라 했는데 어케하나?

#선택자를 이용하는 방법 => 테그이름:nth-of-type(숫자) ->숫자를 1부터 셈/ clas,id 쓸 수 없음 Q. 이게 정확하게 무슨의미?
    #장르
    genre = m.select("dl.lst_dsc dl.info_txt1 dd:nth-of-type(1) a") #뒤에 a까지 쓸 수 있음 -> 첫번째 a라는 뜻
    #감독
    director = m.select("dl.lst_dsc dl.info_txt1 dd:nth-of-type(2) a")
    #배우
    actor = m.select("dl.lst_dsc dl.info_txt1 dd:nth-of-type(3) a")


    for g in genre:                        # Q. 출력시 배우: <- 얘는 한 번만 나오게 하는 법?
        print("장르:", g.text)
    for d in director:
        print("감독:", d.text)
    for a in actor:
        print("배우:",a.text)
    print("=" * 50)
#Q.  line22-> 굳이 왜  span.link_txt로 한거? 원래대로 dl.lst_dsc dl.info_txt1 dd:nth-of-type(1) a 이렇게 해도
#             어차피 리스트로 받는 거니깐 상관 없는 것 아님? span.link_txt-> 얘는 리스트가 아니라 그냥 문자열로 받아들이는 건가?
#              -> 즉 "액션" 안하고 "액"만 써도 된다는 차이?