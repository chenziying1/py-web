import os
import requests
import time

headers = {
          'Host': 'vo1.123188kk.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
          'Accept': '*/*',
          'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
          'Accept-Encoding': 'gzip, deflate, br',
          'Origin': 'https://passummit.com',
          'Connection': 'keep-alive',
          'Referer': 'https://passummit.com/',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'cross-site',
          }
'''
proxy = {
    'http': '183.239.61.167:9091'
}
'''
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
                    elif 'https:' in url and '.key' not in url:
                              #print(url)
                              aurl.append(url)
          urls.append(aurl)
          return urls

#2.实施爬取，并分析
#这里有点担心网络不好而导致下载还没完成就转跳到下一个url有，想用函数稍微等待一下
#出现了速度过慢的问题，查明并不是网络速度的问题，是服务器响应的
def paqu(path,aurls):
          if not os.path.exists(path):
                    os.makedirs(path)
          a = 0
          for url in aurls:
                    a += 1
                    filename = path + 'python链接mysqldemo' + str(a) + '.ts'
                    f = open(filename,"wb")
                    print('爬取 ',url)
                    target = requests.get(url,headers = headers)#,proxies=proxy
                    #print(target)
                    time.sleep(1)
                    if target.status_code == 200:
                              print('写入',filename)
                              f.write(target.content)
                              time.sleep(1)
                              f.close()
                    else:
                              print('写入失败')
                              f.close()
                              continue
                    '''
                    with open() as f:
                              print('爬取 ',url)
                              target = requests.get(url,headers = headers)#,proxies=proxy
                              #
                              if target.status_code == 200:
                                        print('写入',filename)
                                        f.write(target.content)
                                        time.sleep(1)
                              else:
                                        print('写入失败')
                                        f.close()
                                        continue
                    '''        
                    
          print(path+'爬取完成')
          return 

'''for i in range(1,8):
          filename = 'index' + str(i) + '.txt'
          m3u8(filename)
'''

m3u8('index.txt')
          
#urls = m3u8('index.txt')
a = 0
for i in urls:
          a += 1
          strs = str(a)
          path = 'video/' + strs + '/'
          paqu(path,i[0:])
          
#print(len(urls))


