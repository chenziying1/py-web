import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')

print(soup.a.parent)
print(soup.a.parent['id'])
print(soup.a.parents)
