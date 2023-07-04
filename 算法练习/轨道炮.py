# -*- coding: utf-8 -*-
# time:2023/4/15 9:28
# file 轨道炮.py
# outhor:czy
# email:1060324818@qq.com


import os
import sys

# 请在此输入您的代码

n = int(input())
a = []
for i in range(n):
    a.append(list(input().split()))

for i in range(n):
    for k in range(3):
        a[i][k] = int(a[i][k])

ans = 0
for k in range(100):
    i, target,tmp = 0, 0,a[0]
    while i != n:
        if a[i][3] == "R":
            a[i][0] += a[i][2]
        if a[i][3] == "L":
            a[i][0] -= a[i][2]
        if a[i][3] == "D":
            a[i][1] -= a[i][2]
        if a[i][3] == "U":
            a[i][1] += a[i][2]
        if  abs(tmp[0]) == abs(a[i][0]) or abs(tmp[1]) == abs(a[i][1]):
            target += 1
        tmp = a[i]
        i += 1
    ans = max(ans, target)
print(ans)



