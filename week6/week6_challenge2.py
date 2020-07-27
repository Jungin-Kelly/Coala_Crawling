from selenium import webdriver
import time


#1. 웹드라이버 켜기
driver =webdriver.Chrome("./chromedriver")

#2. 구글맵 접속하기
driver.get("https://www.google.com/maps/@37.6003073,126.986331,14z?hl=ko")

#3. 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("input#searchboxinput")
search_box.send_keys("노인정")

#4. 검색버튼 누르기
search_button = driver.find_element_by_css_selector("button#searchbox-searchbutton")
search_button.click()

#5. 검색 결과 확인
time.sleep(5)

#컨테이너: div.section-result-text-content
#가게이름: h3.section-result-title
#평점: span.cards-rating-score
#주소: span.section-result-location
cafes = driver.find_elements_by_css_selector("div.section-result-text-content")
for i in range (10):  #뒤에 부분에 i가 없어도 아래 내용이 (n)번 만큼 반복됨
# 가게이름: h3.section-result-title
    for c in cafes:
        name = c.find_element_by_css_selector("h3.section-result-title").text
        # 가게주소: span.section-result-location
        addr = c.find_element_by_css_selector("span.section-result-location").text
        # 평점:span.cards-rating-score
        try:
            rating = c.find_element_by_css_selector("span.cards-rating-score").text
        except:
            rating = "평점 없음"

        print(name, "/" , addr, "/", rating)


    nextpage= driver.find_element_by_css_selector("span.n7lv7yjyC35__button-next-icon")
    nextpage.click()
#100개 모으는 방법을 모르겠음.  for i in range 5하면 4번 넘어가서 5페이 수집 맞나?
# 평점없어도 오류 안나고 excep, try문 위와 같이 만들었는데 "평점없음"이라는 말도 안뜸
