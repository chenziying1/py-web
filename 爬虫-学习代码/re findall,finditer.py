import re

s1 = "\w*[A-Z]+"

list1 = "wwwwA wwwwwZ"

m = re.findall(s1,list1)
m2 = re.finditer(s1,list1)

for i in m2:
          print(i.group())

print(m)
