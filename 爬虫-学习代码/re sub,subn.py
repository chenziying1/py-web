import re

m1 = re.sub('CZY','czy','i am CZY')
m2 = re.subn('CZY','czy','i am CZY i am CZY')

print(m1)
print(m2)
