# -*- coding: utf-8 -*-
# time:2023/4/6 22:19
# file 三角回文数.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
for i in range(6000,9000):
  k = i*(i+1) // 2
  if k > 20220514 and str(k) == str(k)[::-1]:
    print(k)
    break