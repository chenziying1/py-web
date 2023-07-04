from urllib import request
import base64

url = 'http://localhost:5000/'
headers = {
             'Authorization': 'Basic ' + str(base64.b64encode(bytes('czy:123','utf-8')),'utf-8')
           }
req = request.Request(url = url,headers = headers,method = "GET")
response = request.urlopen(req)
print(response.read().decode('utf-8'))
