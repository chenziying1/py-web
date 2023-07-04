import requests
from bs4 import BeautifulSoup
import re
import csv

header = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
          }

def save_csv(filename,info):
          with open(filename,'a',encoding='utf-8') as f:
                    fieldnames = ['name','author','score']
                    writer = csv.DictWriter(f,fieldnames=fieldnames)
                    writer.writerow(info)

def get_music_info(url):
          html = requests.get(url,headers = header)
          soup = BeautifulSoup(html.text,'lxml')
          name = soup.find(attrs = {'id':'wrapper'}).h1.span.text
          author = soup.find(attrs = {'id':'info'}).find('a').text
          score = soup.find(class_='ll rating_num').text
          info = {'name':name,'author':author,'score':score}
          print(info)
          save_csv('music.csv',info)

def get_url_music(url):
          html = requests.get(url,headers = header)
          soup = BeautifulSoup(html.text,'lxml')
          aTags = soup.find_all("a",attrs = {"class":"nbg"})
          for atag in aTags:
                    get_music_info(atag['href'])


          

urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
with open('music.csv','w',encoding = 'utf-8') as f:
          filename = ['name','author','style','time','publisher','score']
          writer = csv.DictWriter(f,fieldnames=filename)
          writer.writeheader()
for url in urls:
          get_url_music(url)
