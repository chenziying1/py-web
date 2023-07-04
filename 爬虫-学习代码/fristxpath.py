from lxml import etree
tree = etree.parse('13.html',etree.HTMLParser())
title = tree.xpath('/html/head/title')
if len(title)>0:
          print(title[0].text)
