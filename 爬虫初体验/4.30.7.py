# -*- coding: utf-8 -*-
# time:2023/4/30 9:30
# file 4.30.7.py
# outhor:czy
# email:1060324818@qq.com
import requests


def get_data(page_num=1, page_size=20):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }

    data = {
        "cId": 2,
        "devicesupport": 1,
        "page_size": page_size,
        "page_num": page_num,
        "dataTraceId": 880
    }

    url = "http://gprp.4399.com/cg/online/get_h5_ranking.php"

    res = requests.get(url,headers=headers,params=data)

    print(res.json())

if __name__ == '__main__':
    get_data()
    for i in range(2,9):
        print("正在爬取第{}页".format(i))
        get_data(page_num=i)