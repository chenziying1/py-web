# -*- coding: utf-8 -*-
# time:2022/11/13 17:11
# file cookie反爬虫.py
# outhor:czy
# email:1060324818@qq.com

import requests
from lxml import etree

'''
url = "http://www.porters.vip/verify/cookie/content.html"
resp = requests.get(url)
print(resp.status_code)
if resp.status_code == 200:
    html = etree.HTML(resp.text)
    res = html.cssselect('.page-header h1')
    print(res)
else:
    print('this request is fial.')
'''

url = "http://www.porters.vip/verify/cookie/content.html"
header = {'cookie':'isfirst=789kq7uc1pp4c'}
resp = requests.get(url,headers=header)
print(resp.status_code)
if resp.status_code == 200:
    html = etree.HTML(resp.text)
    res = html.cssselect('.page-header h1')[0].text
    print(res)
else:
    print('this request is fial.')