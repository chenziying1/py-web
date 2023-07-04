# -*- coding: utf-8 -*-
# time:2023/4/5 15:32
# file 最小质因子之和.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
n = int(input())

def check(n):
  if n % 2 == 0:
    return 2
  elif n % 3 == 0:
    return 3
  elif n % 5 == 0:
    return 5
  elif n % 7 == 0:
    return 7
  else:
    return n

ans = []
for i in range(n):
  temp = 0
  a = int(input())
  for i in range(2,a+1):
    temp += check(i)
  ans.append(temp)

for i in ans:
  print(i)