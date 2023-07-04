# -*- coding: utf-8 -*-
# time:2023/4/30 9:24
# file 4.30.6.py
# outhor:czy
# email:1060324818@qq.com

import requests

def get_data(page):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    # 请求数据
    payload = {'ac': 'recipe',
               'op': 'getMoreDiffStateRecipeList',
               'classid': '0',
               'orderby': 'hot',
               'page': page}
    url = "https://home.meishichina.com/ajax/ajax.php"
    res = requests.get(url, headers=headers, params=payload)
    # 直接以 JSON 格式返回
    print(res.json())

if __name__ == "__main__":
    get_data(2)
