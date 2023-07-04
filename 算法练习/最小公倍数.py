# -*- coding: utf-8 -*-
# time:2022/12/3 9:48
# file 最小公倍数.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码

n = int(input())
target = [i for i in range(1,n+1)]

def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a%b)

while len(target) != 1:
  a,b = target.pop(0),target.pop(0)
  gongbei = (a*b)//gcd(a,b)
  target.insert(0,gongbei)

print(target[0])


#最小公倍数的求法
# 1.公倍数*公约数=两数乘积
# 2.最小公倍数=两数乘积/公约数