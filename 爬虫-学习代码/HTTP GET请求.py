from urllib3 import *

url = "https://www.baidu.com/s?wd=%E6%B7%98%E5%AE%9D"
http = PoolManager()
response = http.request('GET',url)
print(response.data)
