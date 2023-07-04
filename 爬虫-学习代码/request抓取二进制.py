import requests
from urllib.parse import quote,unquote

r = requests.get('https://img.moegirl.org.cn/common/9/92/70624435_p0.jpg')
print(r.text)
with open('13.png','wb') as fp:
          fp.write(r.content)
