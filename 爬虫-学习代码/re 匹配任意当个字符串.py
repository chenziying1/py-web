import re

s = ".ind"
s2 = "\.ind"
m1 = re.match(s,"bind")
if m1 is not None:
          print(m1.group())

m2 = re.match(s2,"bind")
if m2 is not None:
          print(m2.group())
