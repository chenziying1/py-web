import re

s = "^[a-z]\w*[A-Z]$"
m = re.match(s,"a12313A")
if m is not None:
          print(m.group())
else:
          print("不匹配")
