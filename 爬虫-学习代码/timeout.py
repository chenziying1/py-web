from urllib3 import *

http = PoolManager(timeout=Timeout(connect = 2.0,read = 2.0))

url1 = "https://www.baidu1213213.com/"

try:
          http.request('GET',url1,timeout = Timeout(connect = 2.0,read = 4.0))
except Exception as e:
          print(e)

