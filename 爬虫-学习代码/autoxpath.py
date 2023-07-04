from lxml import etree
import requests

r = requests.get('https://www.jd.com/')

tree = etree.HTML(r.text)

nodes = tree.xpath('//*[@id="navitems-group1"]/li[1]/a/text()')
print(nodes)
