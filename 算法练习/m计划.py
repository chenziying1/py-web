# -*- coding: utf-8 -*-
# time:2023/4/14 8:39
# file m计划.py
# outhor:czy
# email:1060324818@qq.com


import os
import sys

# 请在此输入您的代码
n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))

k=n-m+1

b = 1
for i in range(k):
  print(min(a[b:b+m]))
  b += 1