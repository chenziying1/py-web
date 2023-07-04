import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')

tags = soup.find(id = 'u1')
print(tags)
