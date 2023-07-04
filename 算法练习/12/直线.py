# -*- coding: utf-8 -*-
# time:2023/4/6 15:59
# file 直线.py
# outhor:czy
# email:1060324818@qq.com


data = []
for x in range(3):
    for y in range(4):
            data.append([x,y])

ans = 0
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i] != data[j]:
            ans += 1

print(ans)
