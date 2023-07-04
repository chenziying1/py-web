from urllib3 import *
from re import *

#设置http连接池
http = PoolManager()
#禁用python警告
disable_warnings()

#下载网页
def download(url):
          result = http.request('GET',url)
          htmlstr = result.data.decode('UTF-8')
          print(htmlstr)
          return htmlstr

#解析网页
def analyse(htmlstr):
          alist = findall('<a[^>]*>',htmlstr)
          result = []
          for a in alist:
                    g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]',a)
                    if g != None:
                              url = g.group(1)
                              url = 'http://localhost:81/files/' + url
                              result.append(url)
          return result

#从入口点处抓取html文件的函数
def crawurl(url):
          print(url)
          html = download(url)
          urls = analyse(html)
          for url2 in urls:
                    crawurl(url2)

#在实现的过程中出现了nginx服务器没有成功启动的结果
#在参考了网络上的教程后发现是nginx服务器的80端口被占用的原因
#重新绑定了81端口，发现还是启动不了
#是ul路径的问题，没有设置：81时默认开启80，导致失败，修改后成功
crawurl('http://localhost:81/files')
