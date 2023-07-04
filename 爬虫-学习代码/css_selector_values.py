import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')

tags = soup.select("#u1")
for i in tags:
          tag = i.select('a')
          for j in tag:
                    print(j['href'],j.get_text())
