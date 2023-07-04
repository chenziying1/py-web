from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import json
import requests
from bs4 import *
from lxml import etree
from lxml import *

#保存cokie
'''
def get_info():
          options = webdriver.EdgeOptions()
          #options.add_argument('headless')
          browser = webdriver.Edge('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe',options=options)
          browser.get('https://www.wenku8.net/login.php?jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php')
          name = browser.find_elements(By.CLASS_NAME,'text')[0].send_keys(3337026057)
          password = browser.find_elements(By.CLASS_NAME,'text')[1].send_keys('czy123456')
          login = browser.find_elements(By.CLASS_NAME,'button')[0].click()
          time.sleep(5)
          print('登录成功')
          ul = browser.find_elements(By.CLASS_NAME,'navlist')[0]
          li_list = ul.find_elements(By.TAG_NAME,'li')
          for li in li_list:
                    #print(li.text)
                    a = li.find_element(By.TAG_NAME,'a')
                    #print(a.text)
          dictCookies = browser.get_cookies()
          jsonCookies = json.dumps(dictCookies)
          with open('anquan.txt', 'w') as f:
                    f.write(jsonCookies)
          browser.close()
'''

headers = {
          'Cookie': 'Hm_lvt_d72896ddbf8d27c750e3b365ea2fc902=1660438916; PHPSESSID=t457edbf94k7id2d6hi5uekkk2b8mfhh; jieqiUserInfo=jieqiUserId%3D1125935%2CjieqiUserName%3D3337026057%2CjieqiUserGroup%3D3%2CjieqiUserVip%3D0%2CjieqiUserName_un%3D3337026057%2CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1660438914; jieqiVisitInfo=jieqiUserLogin%3D1660438914%2CjieqiUserId%3D1125935; Hm_lpvt_d72896ddbf8d27c750e3b365ea2fc902=1660438923',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'          
          }

def login():
          url = "http://www.wenku8.net/index.php"
          html = requests.get(url,headers = headers)
          if html.status_code == 200:
                    return html.text
          else:
                    return "登录失败"

def soup(html):
          soups = BeautifulSoup(html,'lxml')
          book_url = soups.select('#centers > div:nth-child(2) > div.blockcontent > div > div:nth-child(2) > a:nth-child(3)')
          url = book_url[0].attrs['href']
          #print(url)
          return url

def get_text(url):
          html = requests.get(url,headers = headers)
          
          soups = BeautifulSoup(html.content,'lxml')
          book_url = soups.select('#content > div:nth-child(1) > div:nth-child(6) > div > span:nth-child(1) > fieldset > div > a')
          url2 = book_url[0].attrs['href']
          
          html2 = requests.get(url2,headers = headers).content
          s = etree.HTML(html2)
          items = s.xpath('//*[@class="css"]/tr')
          print(len(items))
          for item in items:
                    #print(item)
                    #用@的形式去获取标签属性值
                    td = item.xpath('td/a/@href')
                    for a in td:
                              #print(url2[:-10]+'/'+a)
                              zhengwen(url2[:-10]+'/'+a)


def zhengwen(path):
          #global name
          html = requests.get(url = path,headers = headers).content
          soup = BeautifulSoup(html,"html.parser")
          read = soup.find(id='content')
          #防止图片页面捣乱
          if read == None:
                    return 
          title = soup.select('#title')
          '''strs = str(title[0])
          titles = strs[7:-5]
          print(titles)'''
          titles = title[0].text
          #print(type(read.text))
          #bookname = name+'.txt'
          bookname = 'index.txt'
          with open(bookname,'a+',encoding = 'utf-8') as f:
                    f.write(titles + "\n" + read.text + "\n")
          f.close()
          print('爬取完成',titles)

htmls = login()
url = soup(htmls)
get_text(url)

#get_info()          



