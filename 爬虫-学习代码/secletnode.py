import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')
print(html.text)
#print(soup.li.attrs)
print(soup.a['href'])
print(soup.a.string)
