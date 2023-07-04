# -*- coding: utf-8 -*-
# time:2023/4/6 19:08
# file 双阶乘.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
n=eval(input())
for i in range(int(n**0.5)+1,0,-1):
  k= n % (i**2)
  if k==0:
    print(n//(i**2))
    break
