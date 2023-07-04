# -*- coding: utf-8 -*-
# time:2023/4/7 12:21
# file 车牌.py
# outhor:czy
# email:1060324818@qq.com

ans = 0
path = []

def dfs(i):
    global ans,path

    if i == 7:
        flag = True
        for j in range(5,1,-1):
            if path[j] == path[j-1] and path[j-1] == path[j-2]:
                flag = False
        if flag:
            ans += 1
        return

    if i > 3:
        n = 9
    else:
        n = 15

    for k in range(n+1):
        path.append(k)
        dfs(i+1)
        path.pop()

dfs(1)
print(ans)

