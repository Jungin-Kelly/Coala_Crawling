# 셀레니움 연습하기
from selenium import webdriver
import time

#1. 웹드라이버 켜기
driver =webdriver.Chrome("./chromedriver") #./chromedriver -> 현재 폴더에 있는 크롬 드라이브를 열어줘
                                          #파이썬에서 크롬에 접근할 수 있게 해주는 애
#2. 네이버 지도 접속하기
driver.get("https://v4.map.naver.com/") #헤더는 필요없음 b/c이미 driver 사용중

#3. 검색창에 검색어 입력하기// 검색창:input#search-input
search_box = driver.find_element_by_css_selector("input#search-input") #css로 원하는 선택자 선택
search_box.send_keys("치킨") #변수.send_keys("값") -> input 처럼 원하는 지정한 값을 변수 장소에 넣어줌
popup = driver.find_element_by_css_selector("span.img")
popup.click()    #팝업창때메 실행오류떠서 팝업창 클릭 추가함
#4. 검색버튼 누르기 // 검색버튼: button.spm
search_button = driver.find_element_by_css_selector("button.spm") #css로 원하는 선택자 선택
search_button.click() #버튼을 클릭해줘

#5. 검색 결과 확인

# n=1
for n in range(1,5):
    #6. 지연시간주기   Q. 이거 정확하게 하는 이유가 뭐임?
    time.sleep(1)
    # 컨테이너: dl.lsnx_det
    #stores = html.select("dl.lsnx_det")
    stores = driver.find_elements_by_css_selector("dl.lsnx_det") # element-> 한 개 요소만/ elements -> 여러 개를 리스트형식으로
    # 가게이름: dl.lsnx_det dt>a
    for s in stores:
        name = s.find_element_by_css_selector("dt>a").text    #이름, 전화번호, 주소는 다 1개만 있기때문에 elementgka
    # 가게주소: dd.addr                                          +)elements로 하면 list로 받는 거라서 .text안먹힘
        addr = s.find_element_by_css_selector("dd.addr").text
    # 전화번호:dd.tel
        try:
            tel = s.find_element_by_css_selector("dd.tel").text
        except:
            tel = "전화번호 없음"
        print(name, '/', addr ,'/', tel)
    # -> 전화번호 없는 경우가 있어서 오류남 => try except 해줘여함
    # try,except도 for 문 안에 넣어줘야 같이 반복돼서 원하는게 나옴



    #페이지버튼 div.paginate  *
    page_bar = driver.find_elements_by_css_selector("div.paginate > *") # *로 모든 테그 선택
    #page_bar[n+1].click()  # div.paginate > *  -> 모든 테그가 선택되고 리스트형태로 저장이됨. 페이지 넘기는 bar부분
    # n=6인 경우 오류남 blc 6페이지 부터는 다음으로 넘겨야 나옴
    try:
        if n%5 != 0 : # n/5의 나머지가 0이 아니라면
            page_bar[n%5 +1].click()
        else:
            page_bar[6].click() # -> 다음으로 넘어가기 버튼
    except:
        print("수집이 완료되었습니다")
        break #다 수집된 경우 for문을 끝낸다
driver.close()