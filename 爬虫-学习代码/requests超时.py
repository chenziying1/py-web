import requests,requests.exceptions
try:
          r = requests.get("https://hao.360.com/",timeout = (0.001,0.1))
except requests.exceptions.Timeout as e:
          print(e)

try:
          r = requests.get("https://hao.360.com/",timeout = 5)
          print("成功")
except requests.exceptions.Timeout as e:
          print(e)
