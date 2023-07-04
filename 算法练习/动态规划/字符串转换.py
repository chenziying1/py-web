# -*- coding: utf-8 -*-
# time:2023/4/4 16:35
# file 字符串转换.py
# outhor:czy
# email:1060324818@qq.com


import os
import sys

# 请在此输入您的代码

s = "0" + input()
t = "0" + input()
dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
for i in range(len(s)):
  dp[i][0] = i
for j in range(len(t)):
  dp[0][j] = j

for i in range(1,len(s)):
  for j in range(1,len(t)):
    if s[i] == t[j]:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
print(dp[len(s)-1][len(t)-1])