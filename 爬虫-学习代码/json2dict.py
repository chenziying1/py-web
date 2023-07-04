import json
data = {
          'name':'czy',
          'companty':'youkonw',
          'age':34
          }
jsonstr = json.dumps(data)
print(jsonstr)

f = open('products.json','r',encoding = 'utf-8')
jsons = f.read()
json1 = json.loads(jsons)
json2 = eval(jsons)
print(json1)
print(json2)
print(json1[0]['name'])
f.close()
