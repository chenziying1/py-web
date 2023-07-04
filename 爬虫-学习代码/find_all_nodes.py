import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.baidu.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')

'''divtags = soup.find_all('div')
print(divtags)
for divtag in divtags:
          atags = divtag.find_all('a')
          for i in atags:
                    print(i)
'''

'''
ultags = 
print(ultags)
for ultag in ultags:
          atags = ultag.find_all('a')
          for i in atags:
                    print(i)

ultags = soup.find_all(attrs={'id':'u1'})
print(ultags)
for ultag in ultags:
          atags = ultag.find_all('a')
          for i in atags:
                    print(i)
'''

tags = soup.find_all(text = '地图')
print(tags)

