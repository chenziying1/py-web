# -*- coding: utf-8 -*-
# time:2023/4/5 15:53
# file excel地址.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码

n = int(input())

target = []
while n:
  if n % 26 == 0:
    target.append(26)
    n = n // 26
    n -= 1
  else:
    target.append(n % 26)
    n = n // 26

target = target[::-1]

ans = ""
for i in target:
  tmp = chr(ord('A')+i-1)
  ans += tmp
print(ans)