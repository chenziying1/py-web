import requests

url = "https://www.baidu.com/"
r = requests.get(url)
print(r.text)
for key,item in r.cookies.items():
          print(key,"=",item)
