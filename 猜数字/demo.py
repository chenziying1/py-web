# -*- coding: utf-8 -*-
# time:2023/6/10 20:42
# file index.py
# outhor:czy
# email:1060324818@qq.com

import random
target = random.randint(1,100)

a = 5
while a:
    print("你现在有%s次机会"%a)
    a-=1
    number = int(input("请输入数字(1-100):"))
    if number > target:
        print("太大了!")
    elif number < target:
        print("太小了!")
    else:
        print("恭喜你猜对了!")
        exit()
print("次数用完啦!")
