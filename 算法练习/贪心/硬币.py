# -*- coding: utf-8 -*-
# time:2023/4/4 13:40
# file 硬币.py
# outhor:czy
# email:1060324818@qq.com

v = [1,5,10,50,100,500]
c = [3,2,1,3,0,2]
a = 620

ans = 0
for i in range(5,-1,-1):
    t = min(a//v[i],c[i])
    a = a-t*v[i]
    ans += t

print(ans)
