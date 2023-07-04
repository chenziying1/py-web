from urllib3 import *

http = PoolManager()
url = 'http://127.0.0.1:5000/'

while True:
          filename = input('请输入要上传的文件名字（必须在当前目录下）:')
          if not filename:
                    break
          with open(filename,'rb') as fp:
                    fileData = fp.read()
          response = http.request('POST',url,fields = {'file':(filename,fileData)})
          print(response.data.decode('utf-8'))
