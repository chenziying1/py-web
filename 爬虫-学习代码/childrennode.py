from lxml import etree
tree = etree.parse('demo.html',etree.HTMLParser())

nodes = tree.xpath("//li/a")
print('共',len(nodes),'个节点')
for i in range(len(nodes)):
          print(nodes[i].text,end=" ")

print()

nodes = tree.xpath("//ul//a")
print('共',len(nodes),'个节点')
for i in range(len(nodes)):
          print(nodes[i].text,end=" ")

