from lxml import etree

tree = etree.parse('13.html',etree.HTMLParser())

root = tree.getroot()
print(root.tag)
print(root[0][0].text)
