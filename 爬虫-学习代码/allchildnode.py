import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')

for child in soup.body.div.contents:
          print(child)
print()
for child in soup.body.div.children:
          print(child)
print()
for child in soup.body.div.descendants:
          print(child)
