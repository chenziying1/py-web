import json
import dicttoxml

f = open('products.json','r',encoding = 'utf-8')
jsonstr = f.read()

d = json.loads(jsonstr)
print(d)

xmlstr = dicttoxml.dicttoxml(d).decode('utf-8')
print(xmlstr)
f.close()
