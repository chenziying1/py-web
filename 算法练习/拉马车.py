# -*- coding: utf-8 -*-
# time:2023/4/6 9:44
# file 拉马车.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
A = input()
B = input()
z = ""

def op(x,j):
    global z
    if len(x) == 0:
        return False
    ans = True
    front = x[0]
    if front in j:
        i = j.index(front)
        tmp = x[0] + j[:i+1]
        x = x[1:] + tmp[::-1]
        z = j[i+1:]
    else:
        z = j + front
    x = x[1:]
    return ans


flaga = True
flagb = False
while (1):
    if flaga:
        flaga = op(A,z)
        if len(A) == 0:
            print(B)
            break
        flagb = not flaga
    if flagb:
        flagb = op(A, z)
        if len(B) == 0:
            print(A)
            break
        flaga = not flagb

"""temp = ""
while len(A) != 0 and len(B) != 0:
  if temp != "" and A[0] in temp:
    tmp = temp[:temp.index(A[0])+1] + A[0]
    temp = temp[temp.index(A[0])+1:]
    A = A[1:] + tmp[::-1]
    continue
  else:
    temp += A[0]
    A = A[1:]
  if temp != "" and B[0] in temp:
    tmp = temp[:temp.index(B[0])+1] + B[0]
    temp = temp[temp.index(B[0])+1:]
    B = B[1:] + tmp[::-1]
    continue
  else:
    temp += B[0]
    B = B[1:]

if len(A) != 0:
  print(A)
elif len(B) != 0:
  print(B)
else:
  print(-1)"""


