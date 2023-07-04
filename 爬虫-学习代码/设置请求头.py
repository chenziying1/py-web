from urllib import request,parse
url = 'http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
           'Host':'httpbin.org'}
dicts = {
          'name':'bili',
          'age':30
          }
data = bytes(parse.urlencode(dicts),encoding = 'utf-8')
req = request.Request(url = url , data = data,headers = headers)
response = request.urlopen(req)
print(response.read().decode('utf-8'))
