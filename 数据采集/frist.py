# -*- coding: utf-8 -*-
# time:2023/4/23 21:19
# file frist.py
# outhor:czy
# email:1060324818@qq.com

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_tltie(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        obj = BeautifulSoup(html,"lxml")
        lists = obj.find("table",{"id":"giftList"}).tr.next_siblings
    except AttributeError as a:
        return None
    return lists

# https://www.pythonscraping.com/pages/page1.html
#https://www.pythonscraping.com/pages/warandpeace.html
lists = get_tltie("https://www.pythonscraping.com/pages/page3.html")
if lists is None:
    print("Not Fund!")
else:
    for i in lists:
        print(i.get_text())
