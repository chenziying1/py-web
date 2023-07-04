from urllib3 import *
from re import *
http = PoolManager()

def download(url):
          result = http.request('GET',url)
          htmlstr = result.data.decode('utf-8')
          return htmlstr

def anaylse(htmlstr):
          alist = findall('<a[^>]*post-item-title[^>]*>[^<]*</a>',htmlstr)
          result = []
          for a in alist:
                    g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]',a)
                   
                    if g != None:
                              #group（）用来提出分组截获的字符串，（）用来分组
                              url = g.group(1)
                    index1 = a.find(">")
                    #Python rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回 -1。
                    index2 = a.rfind("<")
                    title = a[index1+1:index2]
                    d = {}
                    d['url'] = url
                    d['title'] = title
                    result.append(d)
          return result

def crawler(url):
          html = download(url)
          bolglist = anaylse(html)
          for bolg in bolglist:
                    print('titls:',bolg['title'])
                    print('url:',bolg['url'])

crawler('https://www.cnblogs.com')
                    
