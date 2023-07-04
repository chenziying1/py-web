# -*- coding: utf-8 -*-
# time:2023/6/6 11:42
# file demo.py
# outhor:czy
# email:1060324818@qq.com

"""
需求：
    定时每天爬取某网站的信息并储存
业务逻辑：
    1.在windows系统中创建任务设置好执行的脚本
    2.书写爬取的程序，抓取必要的数据，并保存
"""
import re
import datetime
import requests

url = "https://acgum.com/"
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37'
}
html = requests.get(url,headers=headers)
html.encoding = html.apparent_encoding
text = re.findall('div class="item-body flex xx flex1 jsb"><h2 class="item-heading">(.*?)</div><div>',html.text)
target = ""

for i in text:
    target += i + "\n"

with open(str(datetime.date.today())+".txt","w+",encoding="utf-8") as f:
    f.write(target)
f.close()

print(text)
