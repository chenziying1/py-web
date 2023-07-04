import requests
import re
from bs4 import BeautifulSoup
url = input("请输入需要爬取的小说的url:")

response = requests.get(url)
data_html = response.text

#<a href="2135572.html">第六百八十七章 大结局，最后一个条件</a>
href_list = re.findall('<dd><a href="(.*?)">.*?</a></dd>',data_html)
title = re.findall('<h1>(.*?)</h1>',data_html)[0]


with open(title+'.txt','w+') as f:
          f.close()

for i in href_list[12:]:
          urls = url + i
          #print(urls)
          responses = requests.get(urls)
          data_htmls = responses.text
          #print(data_htmls)
          soup = BeautifulSoup(data_htmls,'lxml')
          tags = str(soup.find_all(id='content')[0])
          tags = tags.replace('<br/>','\n')
          tags = tags.replace('<div>','\n')
          tags = tags.replace('</div>','\n')
          with open(title+'.txt','w+',encoding = 'utf-8') as f:
                    f.write(tags)
          f.close()
          titles = soup.find_all(class_='bookname')
          titles2 = re.findall('<h1>(.*?)</h1>',str(titles))[0]
          print(titles2,'爬取成功')

          
          

