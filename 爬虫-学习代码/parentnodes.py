from lxml import etree
tree = etree.parse('demo.html',etree.HTMLParser())

result = tree.xpath('//a[@href = "123.html"]/../@class')
print(result)
