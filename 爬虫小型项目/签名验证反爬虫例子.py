# -*- coding: utf-8 -*-
# time:2022/11/17 16:48
# file 签名验证反爬虫例子.py
# outhor:czy
# email:1060324818@qq.com

from time import time
from random import randint,sample
import hashlib
import requests

def hex5(value):
    mainpulator = hashlib.md5()
    mainpulator.update(value.encode('utf-8'))
    return mainpulator.hexdigest()

def url_test(action,tim,randstr,hexs):
    url_t = "?actions={0}&tim={1}&randstr={2}&sign={3}".format(action,tim,randstr,hexs)
    return url_t

action = "".join(str([randint(1,9) for _ in range(5)]))
tim = round(time())
randstr = "".join(sample([chr(_) for _ in range(65,91)],5))
value = action+str(tim)+randstr
hexs = hex5(value)
print(action,tim,randstr,hexs)

url = "http://www.porters.vip/verify/sign/fet"+url_test(action,str(tim),randstr,hexs)
resp = requests.get(url)
print(resp.status_code,resp.text)
