from urllib.request import urlopen
import urllib 
data = bytes(urllib.parse.urlencode({'name':'bili','age':30}),encoding = 'utf-8')
reponse = urlopen('http://httpbin.org/post',data=data)
print(reponse.read().decode('utf-8'))
