# -*- coding: utf-8 -*-
# time:2023/4/7 15:55
# file 统计子矩阵.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码

n,m,k = map(int,input().split())
a,s = [[0 for i in range(m+1)]],[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n):
  a.append([0] + list(map(int,input().split())))

for i in range(1,n+1):
  for j in range(1,m+1):
    s[i][j] = s[i][j-1]+s[i-1][j]+a[i][j]-s[i-1][j-1]




ans = 0
for lx in range(1,n+1):
  for rx in range(lx,n+1):
    for ly in range(1,m+1):
      for ry in range(ly,m+1):
        if s[rx][ry] - s[lx-1][ry] - s[rx][ly-1] + s[lx-1][ly-1] <= k:
          ans += 1
print(a)
print(s)
print(ans)


