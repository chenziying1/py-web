# -*- coding: utf-8 -*-
# time:2023/4/30 9:12
# file 4.30.5.py
# outhor:czy
# email:1060324818@qq.com

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'
}

def get_detail():
    r = requests.get("https://labfile.oss.aliyuncs.com/courses/3086/books.html", headers=headers)
    r.encoding = 'utf-8'
    html_doc = r.text
    soup = BeautifulSoup(html_doc, "lxml")
    div_tags = soup.select("div[class='jl-book-item']")
    for item in div_tags:
        bug_link = item.a.attrs["href"]
        img = item.find("img").attrs["src"]
        name = item.select("h3")[0].get_text()
        print(bug_link,img,name)

if __name__ == "__main__":
    get_detail()
