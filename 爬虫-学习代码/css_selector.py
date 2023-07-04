import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')

tags = soup.select('a')[2:]
print(tags)

tags = soup.select('.mnav')
print(tags)

tags = soup.select('#u1')
print(tags)
