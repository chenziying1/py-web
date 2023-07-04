from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import re

pages = set()

def getlink(pagesurl):
          global pages
          headers = {
                    'referer': 'https://zh.wikipedia.ahut.cf/',
                    'cookie': 'GeoIP=VN:::16.17:107.83:v4',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}
          #data=bytes(urllib.parse.urlencode(headers),encoding='utf-8')
          req ='https://zh.wikipedia.ahut.cf{}'.format(pagesurl)
          data1 = urllib.request.Request(req, headers=headers)
          html = urllib.request.urlopen(data1).read()
          #html = urllib.request.urlopen(req,data = data)
          
          bs = BeautifulSoup(html,'html.parser')
          try:
                    print(bs.h1.get_text())
                    print(bs.find(id = 'mw-content-text').find_all('p')[0])
                    print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
          except AttributeError:
                    print("页面缺少一些属性，不过不用担心")

          for link in bs.find_all('a',href=re.compile('^(/wiki/)')):
                    if 'href' in link.attrs:
                              if link.attrs['href'] not in pages:
                                        newpages = link.attrs['href']
                                        print('-'*20)
                                        print(newpages)
                                        pages.add(newpages)
                                        getlink(newpages)


getlink('/wiki/%E4%B9%8C%E5%85%8B%E5%85%B0')
