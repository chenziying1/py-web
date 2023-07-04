import re
m1 = re.match("python","python i love ")
if m1 is not None:
          print(m1.group())
print(m1)

m2 = re.search("python","i love python")
if m2 is not None:
          print(m2.group())
print(m2)
