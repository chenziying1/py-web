# -*- coding: utf-8 -*-
# time:2023/4/4 15:27
# file 完全背包.py
# outhor:czy
# email:1060324818@qq.com
n = 4
w = [2,1,3,2]
v = [3,2,4,2]
W = 5

dp = [[0 for i in range(W+1)]for i in range(n+1)]
for i in range(n):
    for j in range(W+1):
        if j < w[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j],dp[i+1][j-w[i]]+v[i])
print(dp[n][W])
