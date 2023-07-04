from lxml import etree
tree = etree.parse('demo.html',etree.HTMLParser())

alist = tree.xpath('//a[@href = "123.html" or @href = "456.html"]')
for a in alist:
          print(a.text,a.get('href'))
