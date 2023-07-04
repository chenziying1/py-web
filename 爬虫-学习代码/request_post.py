import requests
data = {
          'name' : 'czy'
          }

url = "http://httpbin.org/post"
r = requests.post("http://httpbin.org/post",data = data)
print(r.text)
