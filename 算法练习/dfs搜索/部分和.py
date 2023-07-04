# -*- coding: utf-8 -*-
# time:2023/4/3 15:05
# file 部分和.py
# outhor:czy
# email:1060324818@qq.com

n = 4
k = 13
a = [1,2,4,7]
def dfs(i,sum):
    if(i==n):
        return sum == k
    if(dfs(i+1,sum)):
        return True
    if(dfs(i+1,sum+a[i])):
        return True
    return False

if(dfs(0,0)):
    print("True")
else:
    print("False")
