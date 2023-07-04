from urllib3 import *

http = PoolManager()
url = 'https://www.baidu.com/'

response = http.request('GET',url)
for key in response.info().keys():
          print(key,":",response.info()[key])
