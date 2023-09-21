# -*- coding: utf-8 -*-
# time:2023/6/7 16:37
# file index.py
# outhor:czy
# email:1060324818@qq.com

"""
一共有247页 截止到2023.6.7
网页信息：http://154.84.5.237/forum/archiver/fid-322-page-247.html
内容信息：http://154.84.5.237/forum/archiver/tid-4220893.html

需求：
    获取这247页全部的信息，包括两种，文章名字，文章地址，存入txt文件之中，要用时根据命令行参数进行读取并返回数据
步骤：
    1.发起请求
    2.获取数据
    3.解析数据
    4.保存数据到txt文件
"""

import re
import time

from urllib.error import HTTPError

import requests
from bs4 import BeautifulSoup

url = "http://154.84.5.237/forum/archiver/fid-322-page-200.html"

#0.创建url
def create_url():
    urls = []
    for i in range(0,248):
        url = "http://154.84.5.237/forum/archiver/fid-322-page-%s.html"%(str(i))
        urls.append(url)
    print("url创建完毕 "+urls[-1])
    return urls

# 1.发起请求
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37',
        'Host': '154.84.5.237',
    }
    try:
        html = requests.get(url,headers=headers)
        html.encoding = html.apparent_encoding
    except HTTPError as e:
        print(e)
    print("url获取成功!")
    return html

# 2.获取数据
def get_data(html):
    bfs4 = BeautifulSoup(html.text, "lxml")
    return bfs4

# 3.解析数据
def data(bfs4):
    href,names = [],[]
    data = bfs4.findAll("li")
    for i in data:
        href.append(i.a.text)
        names.append(i.a.get('href'))
    if href is not None and names is not None:
        print("数据解析成功!")
    else:
        print("数据解析失败!")
    return href,names

# 4.保存数据到txt文件
def save_txt(href,names):
    strs = ""
    for i in range(len(href)):
        url,name = "http://154.84.5.237/forum/" + href[i],names[i]
        strs += url + " " + name + "\n"
    with open("data.txt","a+",encoding="utf-8") as f:
        f.write(strs)
    f.close()
    print("文件保存成功!")
    return

if __name__ == "__main__":
    urls = create_url()
    for url in urls:
        print("---------" + url + "----------")
        html = get_html(url)
        bfs4 = get_data(html)
        href,names=data(bfs4)
        save_txt(href, names)
        time.sleep(2)






"""
获取想要内容的方法：
<li><a href="archiver/tid-3696126.html">***** 第三十七章</a> <em>(32 篇回复)</em></li>
<a href="archiver/tid-3696126.html">***** 第三十七章</a>
***** 第三十七章
archiver/tid-3696126.html

i
i.a
i.a.text
i.a.get('href')
"""