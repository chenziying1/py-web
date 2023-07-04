import re

s = "(\d{3})-(\w{3})-(\d{3})"

m = re.match(s,"123-aaa-123")
if m is not None:
          print(m.group())
          print(m.group(1))
          print(m.group(2))
          print(m.group(3))
          print(m.groups())
