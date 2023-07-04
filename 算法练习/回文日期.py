# -*- coding: utf-8 -*-
# time:2022/12/1 10:11
# file 回文日期.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
number = input()
numbers = int(number[:4])

def pandaun(x):
  target = x

  if (int(target[4:6]) > 12 or int(target[4:6]) <= 0) or (int(target[6:8]) > 31 or int(target[6:8]) <= 0):
    return False

  if int(target[4:6]) in [4, 6, 9, 11]:
    if int(target[6:8]) > 30:
      return False

  if int(target[4:6]) == 2:
    if (int(target[:4]) % 4 == 0 and int(target[:4]) % 100 != 0) or (int(target[:4]) % 400 == 0):
      if int(target[6:8]) > 29:
        return False
    else:
      if int(target[6:8]) > 28:
        return False

  return True


ans = numbers-1
while True:
  ans += 1
  huiwen = str(ans) + str(ans)[::-1]
  if pandaun(huiwen) and ans != number:
    break

ans = numbers -1
while True:
  ans += 1
  ab = str(ans) + str(ans)[::-1]
  if ab[0] == ab[2] and ab[1] == ab[3] and pandaun(ab) and ans != number:
    break


print(huiwen)
print(ab)



