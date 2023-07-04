# -*- coding: utf-8 -*-
# time:2023/6/18 16:23
# file demo.py
# outhor:czy
# email:1060324818@qq.com
import requests

url = "https://hanime1.me/comic/91680"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie':'cf_clearance=BreGTQutDUUGnzuRsJWUTcukIaL2GOI7YgEtYL85abI-1687058973-0-160',
}

data = requests.get(url,headers=headers).content

with open("1.jpg","w+") as f:
    f.write(data)
f.close()