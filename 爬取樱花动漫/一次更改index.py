import os

#ffmpeg -allowed_extensions ALL -i C:/Users/HP/Desktop/video/1/index.m3u8 -c copy C:/Users/HP/Desktop/video/1/inew.mp4
target = ['#EXT-X-KEY:METHOD=AES-128,URI="C:/Users/HP/Desktop/video/1/key.key"']

#2.写入新文件
def writefile(strs):
          with open('python链接mysqldemo.txt','a+') as f2:
                    f2.write(strs)
          f2.close()
          return
          


#1.打开被读取文件,处理数据
def openoldfile(name):
          f = open(name,'r+')
          test = 0
          while True:
                    url = f.readline()
                    url = url.rstrip()
                    if url == "":
                              break
                    elif 'https:' in url and '.key' in url:
                              writefile(target[0]+'\n')
                    elif 'https:' in url and '.key' not in url:
                              test += 1
                              writefile('C:/Users/HP/Desktop/video/1/python链接mysqldemo'+str(test)+'.ts'+'\n')
                    else:
                              writefile(url+'\n')
          f.close()
                              
          


openoldfile('index.txt')


