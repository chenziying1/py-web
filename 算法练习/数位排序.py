# -*- coding: utf-8 -*-
# time:2023/4/7 8:09
# file 数位排序.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
n = int(input())
m = int(input())

def shuwei(i):
  a = list(str(i))
  ans = 0
  for b in a:
    ans += int(b)
  return ans

target = []
for i in range(1,n+1):
  he = shuwei(i)
  target.append([he,i])
target.sort()
print(target)
print(target[m-1][1])

