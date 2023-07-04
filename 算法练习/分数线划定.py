# -*- coding: utf-8 -*-
# time:2023/4/11 10:56
# file 分数线划定.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
n,m = map(int,input().split())
a,target = [],round((m*1.5))
for i in range(n):
  a.append(list(map(int,input().split())))
a.sort(key = lambda s:s[1],reverse = True)

ans = []
for i in a:
  if i[1] >= a[target-1][1]:
    ans.append(i)

print(a[target-1][1]," ",len(ans))
for i in range(len(ans)-1):
  if ans[i][1] == ans[i+1][1] and ans[i][0] > ans[i+1][0]:
    ans[i][0],ans[i+1][0] = ans[i+1][0],ans[i][0]
  print(ans[i][0]," ",ans[i][1])
print(ans[len(ans)-1][0]," ",ans[len(ans)-1][1])


