# -*- coding: utf-8 -*-
# time:2023/4/5 16:47
# file 凑包子.py
# outhor:czy
# email:1060324818@qq.com

n = int(input())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

a = [0]
f = [False for i in range(10001)]
f[0] = True
for i in range(1,n+1):
    a.append(int(input()))

    if i == 1:
        g = a[i]
    else:
        g = gcd(a[i],g)

    for j in range(10000-a[i]):
        if f[j]:
            f[j+a[i]] = True
    f[-1] = True
    
ans = 0
if g != 1:
    print("INF")
else:
    for i in range(len(f)):
        if not f[i] :
            ans += 1
    print(ans)
