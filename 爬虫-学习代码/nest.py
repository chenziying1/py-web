import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')
#print(html.text)
print(soup.head)
head = soup.head
print(head.title.string)
print(soup.body.div.a['href'])
