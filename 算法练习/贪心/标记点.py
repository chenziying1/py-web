# -*- coding: utf-8 -*-
# time:2023/4/4 14:51
# file 标记点.py
# outhor:czy
# email:1060324818@qq.com

N = 6
R = 10
x = [1,7,15,20,30,50]

i,ans = 0,0
while i<N:
    s = x[i]
    i += 1
    while i < N and x[i] <= s+R:
        i += 1
    p = x[i-1]
    while i < N and x[i] <= p+R:
        i += 1
    ans += 1
print(ans)