from urllib3 import *

http = PoolManager()
url = 'http://127.0.0.1:5000/register'
response = http.request('POST',url,fields={'name':'李宁','age':'12'})
data = response.data.decode('UTF-8')
print(data)
