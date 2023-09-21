# -*- coding: utf-8 -*-
# time:2023/7/26 0:40
# file test3.py
# outhor:czy
# email:1060324818@qq.com

import json
import requests

with open("cookie.txt","r",encoding="utf-8" ) as f:
    a = f.readline()
    a = a.strip()
f.close()


url = "https://cqchengshigengxin.com/csgx/xmxx/searchZf?pageNum=1&jzqk=00"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie': a,
    'Host': 'cqchengshigengxin.com',
    'Referer': 'http://cqchengshigengxin.com/csgx/xmxx/zf',
}


response = requests.get(url, headers=headers)
# Convert the string to JSON
data = json.loads(response.text)
print(response.text)
# Read the 'id' field values
id_values = [item['id'] for item in data['data']['xmxxList']]
print(id_values)



