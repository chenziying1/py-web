# -*- coding: utf-8 -*-
# time:2023/4/4 15:22
# file 最长公共子序列.py
# outhor:czy
# email:1060324818@qq.com

n,m = 4,4
s = "abcd"
t = "abca"

dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
print(dp[n][m])