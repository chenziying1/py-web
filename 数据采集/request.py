# -*- coding: utf-8 -*-
# time:2023/4/27 20:53
# file request.py
# outhor:czy
# email:1060324818@qq.com
import urllib

import requests
param = {'username': '123', 'password': 'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", data=param)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("-----------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=r.cookies)
print(r.text)