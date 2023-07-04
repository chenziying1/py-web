# -*- coding: utf-8 -*-
# time:2023/4/5 10:06
# file 最长上升子序列.py
# outhor:czy
# email:1060324818@qq.com

n = 5
a = [4,2,3,1,5]
dp = [0 for i in range(n)]
res = 0
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i],dp[j] + 1)
    res = max(res,dp[i])
print(res)