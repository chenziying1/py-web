# -*- coding: utf-8 -*-
# time:2023/4/30 8:20
# file 4.30.2.py
# outhor:czy
# email:1060324818@qq.com
import re

import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}

html = requests.get("https://labfile.oss.aliyuncs.com/courses/3086/lanqiao.html",headers = headers)
html.encoding = 'utf-8'
results = re.findall('<h6 title="(.*)" class="course-name"', html.text)
print(results)