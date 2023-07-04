import os
import requests

headers = {
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
          }
#获取全部的url,每一集的url都已列表的形式存入
urls = []

#1.通过m3u8文件读取到视频地址
def m3u8(filename):
          f = open(filename,'r+')
          url = ''
          aurl = []
          while True:
                    url = f.readline()
                    url = url.rstrip()
                    if url == "":
                              break
                    elif 'https:' in url:
                              #print(url)
                              aurl.append(url)
          urls.append(aurl)
          return urls

#2.实施爬取，并分析
#这里有点担心网络不好而导致下载还没完成就转跳到下一个url有，想用函数稍微等待一下
def paqu(path,aurls):
          if not os.path.exists(path):
                    os.makedirs(path)
          filename = path + aurls[0][56:-4] + '.mp4'
          if os.path.exists(filename):
                    return
          with open(filename,"wb") as f:
                    for url in aurls:
                              target = requests.get(url,headers = headers)
                              f.write(target.content)                    
          f.close()
          print(path+'爬取完成')
          return 

for i in range(1,8):
          filename = 'index' + str(i) + '.txt'
          m3u8(filename)
          
#urls = m3u8('index.txt')
a = 0
for i in urls:
          a += 1
          strs = str(a)
          path = 'video/' + strs + '/'
          paqu(path,i)
          
#print(len(urls))


