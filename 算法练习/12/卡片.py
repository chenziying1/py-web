# -*- coding: utf-8 -*-
# time:2023/4/6 15:50
# file 卡片.py
# outhor:czy
# email:1060324818@qq.com

#3180
target = [2021 for i in range(10)]

for i in range(1,20210):
    tmp = list(str(i))
    for j in tmp:
        target[int(j)] -= 1
    if 0 in target or -1 in target or -2 in target:
        print(i-1)
        break
