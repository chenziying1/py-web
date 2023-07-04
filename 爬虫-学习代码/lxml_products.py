from lxml import etree

tree = etree.parse('products.xml')
root = tree.getroot()
print('root:',root.tag)
chilrens = root.getchildren()
for i in chilrens:
          print('product id = ',i.get('id'))
          print('i[0].name=',i[0].text)
          print('i[1].price = ',i[1].text)
