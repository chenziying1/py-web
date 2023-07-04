# -*- coding: utf-8 -*-
# time:2023/4/7 8:19
# file 考勤打卡.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
n = int(input())

tagret = set()
for i in range(n):
  o = input()[9:]
  tagret.add(int(o))

tagret = list(tagret)
tagret.sort()

for i in tagret:
  print(i)


