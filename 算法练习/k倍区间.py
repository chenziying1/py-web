# -*- coding: utf-8 -*-
# time:2023/4/7 17:58
# file k倍区间.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
n, k = map(int, input().split())
ans = []
for i in range(n):
    ans.append(int(input()))

temp = ans.copy()
for i in range(n - 1):
    ans[i + 1] += ans[i]

number = 0
for i in range(n):
    if temp[i] % k == 0:
        number += 1
    for j in range(i + 1, n):
        if (ans[j] - ans[i-1]) % k == 0:
            number += 1


print(number)


