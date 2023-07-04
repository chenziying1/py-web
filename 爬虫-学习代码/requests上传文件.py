import requests
file = {'file':open('13.png','rb')}
r1 = requests.post("http://127.0.0.1:5000/",files = file)
print(r1.text)
