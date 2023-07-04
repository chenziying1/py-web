from lxml import etree
tree = etree.parse('demo.html',etree.HTMLParser())

nodes = tree.xpath('//*')
print('共',len(nodes),'个节点')
for i in range(len(nodes)):
          print(nodes[i].tag,end=" ")


def printnode(node,intent):
          print(intent + node.tag)
          intent += " "
          children = node.getchildren()
          if len(children) > 0:
                    for i in range(len(children)):
                              printnode(children[i],intent)

print()
printnode(nodes[0],"")

nodes = tree.xpath('//a')
print('共',len(nodes),'个a节点')
for i in range(len(nodes)):
          print(nodes[i].text,end=" ")
