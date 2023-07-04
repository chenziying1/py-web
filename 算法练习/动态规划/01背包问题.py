# -*- coding: utf-8 -*-
# time:2023/4/4 14:58
# file 01背包问题.py
# outhor:czy
# email:1060324818@qq.com

n = 4
w = [2,1,3,2]
v = [3,2,4,2]
W = 5

def rec(i,j):
    res = 0
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i+1,j)
    else:
        res = max(rec(i+1,j),rec(i+1,j-w[i])+v[i])
    return res

ans = rec(0,W)
print(ans)

dp = [[-1 for i in range(W+10)] for i in range(n+10)]
def rec2(i,j):
    if dp[i][j] >= 0:
        return dp[i][j]
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i+1,j)
    else:
        res = max(rec(i+1,j),rec(i+1,j-w[i])+v[i])
    dp[i][j] = res
    return res

print(rec2(0,W))

def rec3():
    dp = [[0 for i in range(W+10)] for i in range(n+10)]
    for i in range(n-1,-1,-1):
        for j in range(W+1):
            if j < w[i]:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j],dp[i+1][j-w[i]]+v[i])
    print(dp[0][W])
rec3()


