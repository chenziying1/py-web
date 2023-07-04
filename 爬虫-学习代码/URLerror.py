#py的url error 一共分为四种情况
from urllib import request,error

try:
          response = request.urlopen("https://www.jb.com/")
except error.URLError as e:
          print(e.reason)
          
