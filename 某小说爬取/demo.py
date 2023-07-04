# -*- coding: utf-8 -*-
# time:2022/12/27 21:51
# file demo.py
# outhor:czy
# email:1060324818@qq.com

import requests
import parsel

'''

'''

def get_data(html):
    selectors = parsel.Selector(html)


def get_html(url):
    rep = requests.get(url)
    if rep.status_code == 200:
        data_html = rep.text
    else:
        data_html = "获取内容失败!"
    return data_html


if __name__ == "__main__":
    URL = ""
    get_html(URL)

