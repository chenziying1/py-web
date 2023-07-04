import re
s = "[ac][bd][ef][rg]"

m1 = re.match(s,"aber")
if m1 is not None:
          print(m1.group())

m2 = re.match(s,"aberi")
if m2 is not None:
          print(m2.group())

m3 = re.match(s,"abei")
if m3 is not None:
          print(m3.group())
