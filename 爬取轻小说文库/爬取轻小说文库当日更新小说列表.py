import requests

from bs4 import BeautifulSoup
from lxml import etree
import re

headers = {
          '__gads':"ID=3ae7ba368ed4a36d-22124053bed50005:T=1661238580:RT=1661238580:S=ALNI_Ma0vZDP3xbKAUq8HuEld_WSxRKNXQ",
          '__gpi':"UID=000008ec8f4a9d82:T=1661238580:RT=1661238580:S=ALNI_MYZ5Fqam-SIrHLRYBd1TTiezKZaGw",
          'Hm_lpvt_d72896ddbf8d27c750e3b365ea2fc902':"1661238583",
          'Hm_lvt_d72896ddbf8d27c750e3b365ea2fc902':"1661238537",
          'jieqiUserInfo':"jieqiUserId=1125935,jieqiUserName=3337026057,jieqiUserGroup=3,jieqiUserVip=0,jieqiUserName_un=3337026057,jieqiUserHonor_un=&#x65B0;&#x624B;&#x4E0A;&#x8DEF;,jieqiUserGroupName_un=&#x666E;&#x901A;&#x4F1A;&#x5458;,jieqiUserLogin=1661238566",
          'jieqiVisitInfo':"jieqiUserLogin=1661238566,jieqiUserId=1125935",
          'PHPSESSID':"upfu5m2crib6mh6hiqti38jb9vc7p34h",
          'Referer':'https://www.wenku8.net/index.php',
          'Cookie': 'Hm_lvt_d72896ddbf8d27c750e3b365ea2fc902=1661238537; Hm_lpvt_d72896ddbf8d27c750e3b365ea2fc902=1661238583; PHPSESSID=upfu5m2crib6mh6hiqti38jb9vc7p34h; jieqiUserInfo=jieqiUserId%3D1125935%2CjieqiUserName%3D3337026057%2CjieqiUserGroup%3D3%2CjieqiUserVip%3D0%2CjieqiUserName_un%3D3337026057%2CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1661238566; jieqiVisitInfo=jieqiUserLogin%3D1661238566%2CjieqiUserId%3D1125935; __gads=ID=3ae7ba368ed4a36d-22124053bed50005:T=1661238580:RT=1661238580:S=ALNI_Ma0vZDP3xbKAUq8HuEld_WSxRKNXQ; __gpi=UID=000008ec8f4a9d82:T=1661238580:RT=1661238580:S=ALNI_MYZ5Fqam-SIrHLRYBd1TTiezKZaGw',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'          
          }

def get_text(url):
          global name
          html = requests.get(url,headers = headers)
          soups = BeautifulSoup(html.content,'html.parser')
          book_url = soups.select('#content > div:nth-child(1) > div:nth-child(6) > div > span:nth-child(1) > fieldset > div > a')
          #tbody不是必须的，虽然在浏览器上渲染了出来，但在代码中体现不出来，因此返回空值的话一定要去掉tbody
          name = soups.select('#content > div:nth-child(1) > table:nth-child(1) > tr:nth-child(1) > td > table > tr > td:nth-child(1) > span > b')[0].get_text()          
          print(name)
          url2 = book_url[0].attrs['href']
          
          html2 = requests.get(url2,headers = headers).content
          s = etree.HTML(html2)
          items = s.xpath('//*[@class="css"]/tr')
          print(len(items))
          for item in items:
                    #用@的形式去获取标签属性值
                    td = item.xpath('td/a/@href')
                    for a in td:
                              zhengwen(url2[:-10]+'/'+a)


def zhengwen(path):
          global name
          html = requests.get(url = path,headers = headers).content
          soup = BeautifulSoup(html,"html.parser")
          read = soup.find(id='content')
          #防止图片页面捣乱
          if read == None:
                    return 
          title = soup.select('#title')
          
          titles = title[0].text
          bookname = name+'.txt'
          with open(bookname,'a+',encoding = 'utf-8') as f:
                    f.write(titles + "\n" + read.text + "\n")
          f.close()
          print('爬取完成',titles)


def get_html(url):
          html = requests.get(url,headers = headers)
          if html.status_code == 200:
                    html.encoding = 'gbk'
                    return html
          else:
                    return "获取失败"

html = get_html('https://www.wenku8.net/modules/article/toplist.php?sort=lastupdate')
hrefs = re.findall('<a style="font-size:13px;" href="(.*?)"',html.text)

for i in hrefs:
          name = ""
          get_text(i)
          




