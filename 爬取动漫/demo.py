# -*- coding: utf-8 -*-
# time:2023/6/11 10:43
# file demo.py
# outhor:czy
# email:1060324818@qq.com
import requests

urls = ["https://s1.xiahi.com/dm/shaonvboziqishui-01.mp4","https://s1.xiahi.com/dm/shaonvboziqishui-02.mp4",
        "https://s1.xiahi.com/dm/shaonvboziqishui-03.mp4","https://s1.xiahi.com/dm/shaonvboziqishui-04.mp4"]


headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

a = 1
for url in urls:
    data = requests.get(url,headers=headers)
    with open(str(a)+".mp4","wb+") as f:
        print("开始爬取"+str(url))
        f.write(data.content)
    f.close()
    a += 1
