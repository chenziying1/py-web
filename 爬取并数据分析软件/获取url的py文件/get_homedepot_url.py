# -*- coding: utf-8 -*-
# time:2023/8/1 14:16
# file get_homedepot_url.py
# outhor:czy
# email:1060324818@qq.com

from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup

with open("../资源/amzon_url.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
f.close()

with open("../资源/cookie.txt", "r", encoding="utf-8") as f:
    b = f.readline()
    b = b.strip()
f.close()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie': b,
}

for url in a:
    url = url.strip()
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    url_list = soup.find_all('a', class_='product-image')
    for a_tag in url_list:
        href = a_tag.get('href')
        with open("../获取home商品数据/homedeport_data.txt", "a+", encoding="utf-8") as f:
            f.write("https://www.homedepot.com"+href+"\n")
            print("https://www.homedepot.com"+href)
        f.close()