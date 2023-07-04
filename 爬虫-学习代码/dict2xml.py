import dicttoxml
from xml.dom.minidom import parseString
import os

d = [20,'names',{'name':'czy','age':20,'salary':2500},{'name':'czy2','age':25,'salary':3500},{'name':'czy3','age':30,'salary':4500}]
bxml = dicttoxml.dicttoxml(d,custom_root = 'persons')
xml = bxml.decode('utf-8')
print(xml)
dom = parseString(xml)
prettyxml = dom.toprettyxml(indent = ' ')
f = open('persons.xml','w',encoding = 'utf-8')
f.write(prettyxml)
f.close()
