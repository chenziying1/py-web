# -*- coding: utf-8 -*-
# time:2023/1/9 15:11
# file demo.py
# outhor:czy
# email:1060324818@qq.com

import requests
import parsel
import tkinter

#1.获取页面代码
def get_html(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
    req = requests.get(url,headers=headers)
    if req.status_code == 200:
        data_html = req.text
    else:
        data_html = "获取页面失败!"
    return data_html

#2.分析处理页面
def get_data(html):
    selectors = parsel.Selector(html)
    wendu = selectors.css(".now b::text").get()
    tianqi = selectors.css("span b::text").get()
    return wendu,tianqi

#3.在exe中显示天气
def mian_windows(wendu,tianqi):
    root = tkinter.Tk()
    root.configure(bg="black")

    listb = tkinter.Label(root,text = "温度："+wendu,font=("ds-digital",40),background="black",
                          foreground="cyan",justify="left")
    listb2 = tkinter.Label(root,text = "天气："+tianqi,font=("ds-digital",40),background="black",
                           foreground="cyan",justify="left")


    listb.pack()
    listb2.pack()
    root.mainloop()



if __name__ == "__main__":
    url = "https://www.tianqi.com/zhanjiang/today/"
    data_html = get_html(url)
    if data_html == "获取页面失败!":
        print("获取失败!")
    else:
        wendu,tianqi = get_data(data_html)
        mian_windows(wendu,tianqi)


