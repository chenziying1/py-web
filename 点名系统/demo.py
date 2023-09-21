# -*- coding: utf-8 -*-
# time:2023/6/7 22:43
# file index.py
# outhor:czy
# email:1060324818@qq.com

"""
需求：
    用Django实现一个点击按钮，就随机返回一个对象
实现：
    前端：
        页面显示所有的学生，点击按钮时，通过发送get请求刷新页面，显示被选中的学生
    后端：
        1.接收请求 get
        2.处理数据
        3.返回响应
"""

import random

number = ['桐人','亚诗娜','爱丽丝']

for i in range(5):

    txt = random.choice(number)

    print(txt)