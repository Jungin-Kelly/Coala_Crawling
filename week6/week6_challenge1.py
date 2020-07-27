from selenium import webdriver
import time

sentence = input("번역하고 싶은 문장을 입력하시오")

#1.web driver켜기
driver =webdriver.Chrome("./chromedriver")

#2. 파파고 들어가기
driver.get("https://papago.naver.com/")
time.sleep(1)        #Q.time.sleep안넣으면 오류가 생김 -> b/c 창이 안떴는데 계속 명령때리면 못알아 먹음
#3. 번역할 내용 입력하기
translate_box = driver.find_element_by_css_selector("textarea#txtSource")
translate_box.send_keys(sentence)

#4. 번역버튼 누르기
button = driver.find_element_by_css_selector("button#btnTranslate")
button.click()
time.sleep(1)
#5.번역내용 확인하기
result = driver.find_element_by_css_selector("div#txtTarget").text
print("번역전:", sentence)
print("번역결과:", result)

driver.close()