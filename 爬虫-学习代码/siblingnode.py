import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')

print(soup)

seconddiv = soup.body.div.next_sibling.next_sibling
print(seconddiv)



seconddiv = soup.div.next_sibling
print(seconddiv.text)#看来是默认查找最后一个div
print(seconddiv.previous_sibling)

for previous in seconddiv.previous_siblings:
          print(previous)
