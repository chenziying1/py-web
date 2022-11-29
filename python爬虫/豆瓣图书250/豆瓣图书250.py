import requests
from lxml import etree


def getonepage(url):
          try:
                    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
                    res = requests.get(url,headers=headers)
                    if res.status_code == 200:
                              return res.text
                    return None
          except Exception:
                    return None

def parseonepage(html):
          selector = etree.HTML(html)
          items = selector.xpath('//tr[@class="item"]')
          ans = []
          for item in items:
                    book_info = item.xpath('td/p/text()')[0]
                    name = item.xpath('td/div/a/@href')[0]
                    ans.append([book_info,name])
          
          return ans
                    
def save(item):
          with open('top250.txt','at',encoding='utf-8') as f:
                    f.write(item)
          f.close()

def getTop250(url):
          html = getonepage(url)
          #print(html)
          for item in parseonepage(html):
                    print(item)
                    save(str(item))

urls = ["https://book.douban.com/top250?start={0}".format(str(i)) for i in range(0,250,25)]
for i in urls:
          getTop250(i)
