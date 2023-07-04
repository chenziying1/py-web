import json
class Product:
          def __init__(self,name,price,age):
                    self.name = name
                    self.price = price
                    self.age = age

def class2json(obj):
          return {
                    'name':obj.name,
                    'price':obj.price,
                    'age':obj.age,
                    }

product = Product('czy',3400,25)

jsonstr = json.dumps(product,default = class2json)
print(jsonstr)
