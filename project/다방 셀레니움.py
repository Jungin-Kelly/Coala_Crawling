from selenium import webdriver
import time

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome("./chromedriver")


driver.get("https://www.dabangapp.com/room/5e09e957def94f4059b921ef")

option = driver.find_elements_by_css_selector("div.styled__Wrap-sc-12s3wwr-1.dDctva")

for s in option:
    # 가게 이름 데이터 수집 // h3.section-result-title
    options = s.find_element_by_css_selector("div.styled__Option-sc-12s3wwr-2 gqtsIc.p").text
    print(options)

driver.close()