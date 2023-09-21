# -*- coding: utf-8 -*-
# time:2023/7/22 22:46
# file index.py
# outhor:czy
# email:1060324818@qq.com

import requests
from bs4 import BeautifulSoup

import time

timestamp = int(time.time())

# 设置请求的URL和参数
url = 'http://api.map.baidu.com/traffic/v1/road'
params = {
    'city':'昆明市',
    'road_name': '北三环',#二环东路,二环北路,二环西路,二环南路,彩云北路,彩云中路,彩云南路,金色大道,北辰大道,昌宏路,广福路,西三环
    'ak': 'W16W0C5FSsLloaq8Z6HjHphu48GMvKu5',
    'timestamp': timestamp
}

# 发送请求并解析json数据
response = requests.get(url, params=params)
json_data = response.json()
print(json_data)
congestion_data = json_data['congestion'][0]

# 解析数据并输出
print(congestion_data['road_name'])
print(congestion_data['traffic_condition'])
