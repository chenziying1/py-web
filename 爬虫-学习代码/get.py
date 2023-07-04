import requests
data = {
          'name':'bili',
          'county':'中国'
        }
r = requests.get('http://httpbin.org/get?',params = data)
print(r.text)
