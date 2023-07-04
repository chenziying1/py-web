# -*- coding: utf-8 -*-
# time:2023/4/3 9:18
# file 杨辉三角.py
# outhor:czy
# email:1060324818@qq.com


def c(a,b):
    res = 1
    i = a
    for j in range(1,b+1):
        res = res * (i / j)
        i -= 1
        if (res > n):
            return res
    return res

def check(k):
    l = 2*k
    r = max(n,l)
    while(l < r):
        mid = (l+r)//2
        if c(mid,k) >= n:
            r = mid
        else:
            l = mid+1
    if c(r,k) != n:
        return False
    print((r+1)*r//2+k+1)
    return True

def mian():
    global n
    n = eval(input())
    for i in range(16,0,-1):
        if check(i):
            break

mian()

