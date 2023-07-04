import json

class Product:
          def __init__(self,d):
                    self.__dict__ = d


f = open('products.json','r')
jsonstr = f.read()

my1 = json.loads(jsonstr,object_hook=Product)
print('name:',my1[0].name)

def json2Product(d):
          return Product(d)

my2 = json.loads(jsonstr,object_hook=json2Product)
print('name:',my2[0].name)

f.close()
