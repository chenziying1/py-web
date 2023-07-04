# -*- coding: utf-8 -*-
# time:2023/4/6 17:10
# file 左孩子有兄弟.py
# outhor:czy
# email:1060324818@qq.com

n = int(input())
target = [[]for i in range(n)]
for i in range(2,n+1):
    v = int(input())
    target[v].append(i)

def dfs(i):
    if len(target[i]) == 0:
        return 0

    maxn = 0
    for j in target[i]:
        maxn = max(maxn,dfs(j))

    return len(target[i]) + maxn

ans = dfs(1)
print(ans)
