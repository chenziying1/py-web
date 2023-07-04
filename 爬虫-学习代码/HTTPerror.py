from urllib import request,error
import socket

try:
          response = request.urlopen('https://bbbccc.com/',timeout = 2)
except error.HTTPError as e:
          print('error.HTTPError:',e.reason)
except error.URLError as e:
          print(type(e.reason))
          print('error.URLError:',e.reason)
          if isinstance(e.reason,socket.timeout):
                    print('超时错误')
          
