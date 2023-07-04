# -*- coding: utf-8 -*-
# time:2022/11/17 17:14
# file 破解有道翻译.py
# outhor:czy
# email:1060324818@qq.com
import json
from time import time
from random import randint,sample
import hashlib
import requests

i = input("请输入要翻译的内容:")
#0.具体post请求需要发送的参数，lts、bv、salt、sign是动态变化的
datas = {
    'i': i,
    'from': 'zh-CHS',
    'to': 'en',
    'smartresult':'dict',
    'client': 'fanyideskweb',
    'salt': '16686758920499',
    'sign': 'd8c8472fb5380cd91291bb91bce66848',
    'lts': '1668675892049',
    'bv': '37dd3c60883fcf3fdfbbfa8fa2c4565d',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}


#1.进行变化参数的设定
def dongtai():
    lts = int(time()*1000)
    salt = str(lts)+str(randint(1,10))

    mainpulator = hashlib.md5()
    mainpulator.update(("fanyideskweb" + datas['i'] +salt + "Ygy_4c=r#e#4EX^NUGUc5").encode('utf-8'))
    sign=mainpulator.hexdigest()
    return lts,salt,sign

#2.写入参数
def write_chang():
    lts, salt, sign = dongtai()
    datas['lts'] = lts
    datas['salt'] = salt
    datas['sign'] = sign
    return datas

url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
'Origin': 'https://fanyi.youdao.com',
'Referer': 'https://fanyi.youdao.com/',
'Cookie': 'OUTFOX_SEARCH_USER_ID=1258733059@10.110.96.153; OUTFOX_SEARCH_USER_ID_NCOO=215789240.04730287; ___rl__test__cookies=1668678419239',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'
}
data=write_chang()
#print(data)
resp = requests.post(url,data=write_chang(),headers=headers)
content = json.loads(resp.text)
print(resp.status_code,content['translateResult'][0][0]['tgt'])








