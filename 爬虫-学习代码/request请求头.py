import requests
from urllib.parse import quote,unquote
headers = {
          'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
          'name' : quote('李宁')
          }
r = requests.get('http://httpbin.org/get',headers = headers)
target = r.text
temp = target.index("name")
print(target[temp:])
