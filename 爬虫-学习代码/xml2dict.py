import xmltodict
f = open('persons.xml','rt',encoding='utf-8')
xml = f.read()
d = xmltodict.parse(xml)
print(d)
f.close()
