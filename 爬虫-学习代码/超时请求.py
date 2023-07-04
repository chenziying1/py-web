import urllib.request
import socket
import urllib.error

try:
          reponse = urllib.request.urlopen('http://httpbin.org/get',timeout = 0.1)
except urllib.error.URLError as e :
          #用e.reason打印出来的结果就是timeout
          print(e.reason)
          #这个也可以使用
          if isinstance(e.reason,socket.timeout):
                    print('超时')
print('1')
