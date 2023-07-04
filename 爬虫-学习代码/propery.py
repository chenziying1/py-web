from lxml import etree
tree = etree.parse('demo.html',etree.HTMLParser())

result = tree.xpath('//a[@href = "123.html"]')
print(result[0].text)

result = tree.xpath('//a[contains(@href,"123")]')
print(result[0].text)

result = tree.xpath('//a[contains(@href,"123")]/@href')
print(result)
