# -*- coding: utf-8 -*-
# time:2023/4/5 10:47
# file 最长公共子序列02.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[0 for i in range(n)] for j in range(m)]

for i in range(m):
  for j in range(n):
    if b[i] == a[j]:
      dp[i][j] = 1
      for k in range(j):
        if a[k] < b[i]:
          dp[i ][j] = max(dp[i][j], dp[i][k] + 1)
    else:
      dp[i][j] = max(dp[i-1][j],dp[i][j-1])



res=dp[m-1][:]
for i in range(0,m):
    res.append(dp[i][n-1])

print(max(res))
