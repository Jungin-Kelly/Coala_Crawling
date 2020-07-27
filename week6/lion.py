from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/maps")
word = "치킨"
search_box = driver.find_element_by_css_selector("input#searchboxinput")
search_box.send_keys(word)
driver.find_element_by_css_selector("searchbox-searchbutton").click()
time.sleep(2)

container = driver.find_elements_by_css_selector("div.section-result-title-container.GLOBAL__gm2-subtitle-alt-1")
for con in container:
    name = con.find_elements_by_css_selector("span.section-result-title-text")
    print(name)
time.sleep(2)
driver.close()