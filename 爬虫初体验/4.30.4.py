# -*- coding: utf-8 -*-
# time:2023/4/30 9:04
# file 4.30.4.py
# outhor:czy
# email:1060324818@qq.com

import requests
from lxml import html




"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# 从网络获取的图片，本实验中表示从本地存储的 HTML 读取的数据
def get_pokemons_fromfile():
    try:
        with open("./target.html", "r", encoding="utf-8") as f:
            data = f.read()
            return data
    except Exception as e:
        return None

def analysis(data):
    # 将网页源码格式化成 element 对象
    page_tree = html.fromstring(data)
    print(page_tree)
    print(type(page_tree))
    # 通过 CSS 选择器获取 所有 title 标签
    eles = page_tree.cssselect('title')
    print(eles)
    print(type(eles))
    # 获取 title 标签内文本
    print(eles[0].text)

if __name__ == "__main__":
    data = get_pokemons_fromfile()
    analysis(data)
    出现了 TypeError: expected string or bytes-like object这样的问题
    """

