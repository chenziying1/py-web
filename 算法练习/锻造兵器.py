# -*- coding: utf-8 -*-
# time:2023/4/12 8:31
# file 锻造兵器.py
# outhor:czy
# email:1060324818@qq.com


import os
import sys

# 请在此输入您的代码
n, c = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
j = 0
i = 0
while i < len(a):
    if abs(a[j] - a[i]) == c:
        ans += 1
    elif j == n - 1:
        i += 1
        j = i + 1
    else:
        j += 1

print(ans)
