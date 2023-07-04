import requests
import os
from bs4 import *
from lxml import etree
from lxml import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 



name = input("请输入你想要获取的小说的名称（不支持模糊查询）:")
headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
          }

#0.按名字查找小说
def find(names):
          options = webdriver.EdgeOptions()
          options.add_argument('headless')
          browser = webdriver.Edge("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\msedgedriver.exe",options=options)
          browser.get('http://www.eshu9.org/')
          time.sleep(5)
          browsers = browser.find_element(By.NAME,'searchkey')
          browsers.click()
          browsers.send_keys(names)
          #<li ka="sel-city-101040100" class="">重庆</li>
          #https://www.zhipin.com/web/geek/job?query=python&city=100010000
#<i class="icon-close"></i>
          browser.find_element(By.CLASS_NAME,'so_book').click()
          time.sleep(3)
          browser.switch_to.window(browser.window_handles[1])
          url = browser.current_url
          #print(url)
          browser.close()
          into(url)


#1.进入小说主页面，进而转跳到目录
def into(urls):
          #TypeError: object of type 'Response' has no len()
          #1.出现错误的原因是因为这里的html是requests对象，无法用BeautifulSoup解析，可以在html后面加上content
          html = requests.get(url = urls,headers = headers).content
          soup = BeautifulSoup(html,"html.parser")
          read = soup.find(class_='read')
          #2.通过.attrs['href']方式打印属性值出来
          click = read.attrs['href']
          #print(click)
          mulu(click)
          
#2.获取章节名称，并转跳章节页面
def mulu(clicks):
          html = requests.get(url = clicks,headers = headers).content
          s = etree.HTML(html)
          items = s.xpath('//*[@id="at"]/tr')
          #print(items)
          for item in items:
                    #print(item)
                    #用@的形式去获取标签属性值
                    td = item.xpath('td/a/@href')
                    for a in td:
                              #print(clicks+a)
                              zhengwen(clicks+a)
          
          



#3.获取正文内容并存入
def zhengwen(path):
          global name
          html = requests.get(url = path,headers = headers).content
          soup = BeautifulSoup(html,"html.parser")
          read = soup.find(id='contents')
          title = soup.select('#amain > dl > dd:nth-child(2) > h1')
          '''strs = str(title[0])
          titles = strs[7:-5]
          print(titles)'''
          titles = title[0].text
          #print(type(read.text))
          bookname = name+'.txt'
          with open(bookname,'a+',encoding = 'utf-8') as f:
                    f.write(titles + "\n" + read.text + "\n")
          f.close()
          print('爬取完成',titles)
          
find(name)
