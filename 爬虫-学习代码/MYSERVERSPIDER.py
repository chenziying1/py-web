import requests
import json
from lxml import etree

result = requests.get('http://localhost:1234/data')
text = result.text
data = json.loads(text)
print("个数：",len(data))
for values in data:
          print(values['name'])
