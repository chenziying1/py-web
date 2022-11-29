import re
m = re.match('hello','hello world')
if m is not None:
          print(m.group())
          print(m)


m2 = re.match("hello","world")
if m2 is None:
          print("匹配失败")
