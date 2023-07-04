# -*- coding: utf-8 -*-
# time:2023/4/6 9:00
# file 九宫幻方.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys
from itertools import permutations
# 请在此输入您的代码

s = [1,2,3,4,5,6,7,8,9]
m = []
for i in range(3):
  m.extend(map(int,input().split()))

def check1(p):
  for j in range(len(m)):
    if m[j] != 0 and p[j] != m[j]:
      return False
  return True

def check2(i):
  if i[0]+i[1]+i[2] == i[3]+i[4]+i[5] == i[6]+i[7]+i[8] == i[0]+i[3]+i[6] == i[1]+i[4]+i[7] == i[2]+i[5]+i[8] == i[0]+i[4]+i[8] \
     == i[2]+i[4]+i[6] == 15 :
    return True
  return False

flag = False
for i in permutations(s):
  p = list(i)
  if check1(p):
    if check2(p):
      ans = p
      flag = True

if flag:
  for i in range(3):
    print(" ".join(str(j) for j in ans[i * 3:i * 3 + 3]))
else:
  print("Too Many")


