import re

s = "bili|czy"

m1 = re.search(s," i love bili or czy")
if m1 is not None:
          print(m1.group())
