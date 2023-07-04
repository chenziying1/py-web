# -*- coding: utf-8 -*-
# time:2023/4/5 9:42
# file 多重部分和.py
# outhor:czy
# email:1060324818@qq.com

n = 3
a = [3,5,8]
m = [3,2,2]
k = 12

dp = [[-1 for i in range(13)]for j in range(13)]
dp[0][0] = 0

for i in range(n):
    for j in range(k+1):
        if dp[i][j] >= 0:
            dp[i+1][j] = m[i]
        elif (j < a[i]) or (dp[i+1][j-a[i]] <= 0):
            dp[i+1][j] = -1
        else:
            dp[i+1][j] = dp[i+1][j-a[i]]-1

print(dp)
if dp[n][k] >= 0:
    print("yes")
else:
    print("no")