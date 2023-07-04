# -*- coding: utf-8 -*-
# time:2023/4/30 8:32
# file 4.30.3.py
# outhor:czy
# email:1060324818@qq.com
import re
import time
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36"
}

def save_img(img_url, name):
    img_res = requests.get(url=img_url, headers=headers)
    # 比对返回的状态码
    if img_res.status_code == requests.codes.ok:
        data = img_res.content
        with open("{name}.png".format(name=name), "wb") as f:
            f.write(data)
        print("{name} - 图片存储完毕".format(name=name))

def get_item(page):

    url =  "http://app.mi.com/topList?page={page}".format(page=page)

    res = requests.get(url,headers=headers)
    if res.status_code == requests.codes.ok:
        html = res.text
        html = re.sub(">\s*<", "><", html)
        # 编译正则表达式，生成一个正则表达式（ Pattern ）对象
        pattern = re.compile(
            r'<li><a href="/details.*?"><img data-src="(.*?)" src=".*?" alt=".*?" width=".*?" height=".*?"></a><h5><a href=".*?">(.*?)</a></h5><p class=".*?"><a href=".*?">(.*?)</a></p></li>')
        items = pattern.findall(html)
        # m.group(0) 返回整个匹配的字符串
        # print(items)
        for item in items:
            # item 数据为 ('图片地址', '我的世界夏季版', '休闲创意')
            save_img(item[0], item[1])


if __name__ == '__main__':
    for page in range(1,43):
        print("正在爬取第{}页".format(page))
        get_item(page)
        time.sleep(2)
