import threading
import datetime
import requests
from bs4 import BeautifulSoup
import re
import time


starttime = datetime.datetime.now()
lock = threading.Lock()

headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
          }

def get_url():
          global urls
          lock.acquire()
          if len(urls) == 0:
                    lock.release()
                    return ""
          else:
                    url = urls[0]
                    del urls[0]
          lock.release()
          return url

def get_url_music(url,thread_name):
          html = requests.get(url,headers=headers)
          soup = BeautifulSoup(html.text,'lxml')
          aTags = soup.find_all("a",attrs = {"class":"nbg"})
          for aTag in aTags:
                    get_music_info(aTag['href'],thread_name)
def get_music_info(url,thread_name):
          html = requests.get(url,headers=headers)
          soup = BeautifulSoup(html.text,'lxml')
          name = soup.find(attrs = {'id':'wrapper'}).h1.span.text
          author = soup.find(attrs = {'id':'info'}).find('a').text
          time = re.findall('发行时间:</span>&nbsp;(.*?)<br>',html.text,re.S)[0].strip()
          info = {
                    'name':name,
                    'author':author,
                    'time':time
                    }
          print(thread_name,info)

class SpiderThread(threading.Thread):
          def __init__(self,name):
                    threading.Thread.__init__(self)
                    self.name = name
          def run(self):
                    while True:
                              url = get_url()
                              if url != "":
                                        get_url_music(url,self.name)
                              else:
                                        break

url_index = 0
urls = ["https://music.douban.com/top250?start={}".format(str(i)) for i in range(0,100,25)]
print(len(urls))

thread1 = SpiderThread('thread1')
thread2 = SpiderThread('thread2')
thread3 = SpiderThread('thread3')
thread4 = SpiderThread('thread4')

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print("退出爬虫")
endtime = datetime.datetime.now()
print('需要时间',(endtime-starttime).seconds,'喵')
