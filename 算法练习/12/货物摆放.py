# -*- coding: utf-8 -*-
# time:2023/4/6 16:12
# file 货物摆放.py
# outhor:czy
# email:1060324818@qq.com


n = 2021041820210418

ans = 0
target = set()
target.add(1)
target.add(n)

for i in range(2,n//2+1):
    target.add(i)
    target.add(n//i)

for i in iter(target):
    for j in iter(target):
        number = n//i//j
        if number*i*j == n:
            ans += 1

print(ans)

