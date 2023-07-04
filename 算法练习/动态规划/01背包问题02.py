# -*- coding: utf-8 -*-
# time:2023/4/5 9:29
# file 01背包问题02.py
# outhor:czy
# email:1060324818@qq.com


n = 4
w = [2,1,3,2]
v = [3,2,4,2]
W = 5

dp = [[100000 for i in range(4*3+1)]for j in range(100)]
dp[0][0] = 0

for i in range(n):
    for j in range(12+1):
        if j < v[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j],dp[i][j-v[i]]+w[i])
res = 0
for i in range(13):
    if dp[n][i] <= W:
        res = i

print(res)