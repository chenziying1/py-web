# -*- coding: utf-8 -*-
# time:2023/4/5 14:16
# file 辗转相除法.py
# outhor:czy
# email:1060324818@qq.com

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(2,7))
