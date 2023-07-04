from lxml import etree
#tree = etree.parse('demo.html',etree.HTMLParser())


tree = etree.parse('demo2.html',etree.HTMLParser())
#tree = etree.HTML('demo2.html')
a1 = tree.xpath('//a[1]/text()')
a2 = tree.xpath('//a[2]/text()')
a3 = tree.xpath('//a/text()')

print(a1,a2,a3)

lasta = tree.xpath('//a[last()]/text()')
print(lasta)

lasta = tree.xpath('//a[position()>1]/text()')
print(lasta)

lasta = tree.xpath('//a[position()=1]/text()')
print(lasta)


