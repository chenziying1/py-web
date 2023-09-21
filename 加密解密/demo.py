# -*- coding: utf-8 -*-
# time:2023/6/10 7:23
# file index.py
# outhor:czy
# email:1060324818@qq.com
import base64
import pickle

target = "123456"

#python->bytes
s = pickle.dumps(target)
print(s)

#bytes->64编码之后->bytes
b = base64.b64encode(s)
print(b)

#bytes->64解码之后->bytes
s = base64.b64decode(b)
print(s)

#bytes->python
s = pickle.loads(s)
print(s)

