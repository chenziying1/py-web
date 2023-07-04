# -*- coding: utf-8 -*-
# time:2023/4/5 10:11
# file 划分数.py
# outhor:czy
# email:1060324818@qq.com

n,m = 4,3
N = 10000

dp = [[0 for i in range(n+1)]for j in range(m+1)]
dp[0][0] = 1
for i in range(1,m+1):
    for j in range(n+1):
        if j - i >= 0:
            dp[i][j] = (dp[i-1][j]+dp[i][j-1])%N
        else:
            dp[i][j] = dp[i-1][j]
print(dp[m][n])
