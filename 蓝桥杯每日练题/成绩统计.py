# -*- coding: utf-8 -*-
# time:2022/11/30 11:30
# file 成绩统计.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
numbers = int(input())
target = []
for i in range(numbers):
  target.append(int(input()))


a,b = 0,0
for i in target:
  if i >= 60 and i < 85:
    b += 1
  if i >= 85:
    a += 1


print("{}%".format(round(((b+a)/numbers)*100)))
print("{}%".format(round((a/numbers)*100)))

