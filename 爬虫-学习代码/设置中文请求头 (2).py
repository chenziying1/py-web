from urllib import request
from urllib.parse import unquote,urlencode
import base64

url = 'http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
           'Host':'httpbin.org',
           'chinese1':urlencode({'name':'李宁'}),
           #b64encode编码
           'chinese2':base64.b64encode(bytes('中文请求HTTP头',encoding = 'utf-8'))
           }
dicts = {
          'name':'bili',
          'age':30
          }

data = bytes(urlencode(dicts),encoding = 'utf-8')
req = request.Request(headers = headers,data = data,url = url)
response = request.urlopen(req)
value = response.read().decode('utf-8')
print(value)

import json
responsejson = json.loads(value)
print(unquote(responsejson['headers']['Chinese1']))
#b64decode解码
print(str(base64.b64decode(responsejson['headers']['Chinese2']),'utf-8'))
print("hrllo world!")
