from xml.etree.ElementTree import parse

tree = parse('products.xml')

for item in tree.iterfind('products/product'):
          id = item.findtext('id')
          name = item.findtext('name')
          price = item.findtext('price')
          print('uuid = ',item.get('uuid'))
          print('id = ',id)
          print('name = ',name)
          print('price = ',price)
          print()
