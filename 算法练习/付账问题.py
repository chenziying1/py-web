# -*- coding: utf-8 -*-
# time:2023/4/6 14:52
# file 付账问题.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys
n,s=map(int,input().split())
a=list(map(int,input().split()))
ave=s/n#计算平均值
a.sort()#排序
b=0
for i in range(n):
    if a[i]<=s/(n-i):
        b+=pow(a[i]-ave,2)#计算平方差
    else:
        b+=pow(s/(n-i)-ave,2)*(n-i)
        break
    s-=a[i]

b=(b/n)**0.5
print("{:.4f}".format(b))#输出最小标准差
