import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.dabangapp.com/room/5e0d7909f22474545f101a5e",headers ={"User-Agent":"Mozilla/5.0"})

html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.styled__Wrap-sc-12s3wwr-1.dDctva.p")
print(container)
