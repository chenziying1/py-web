# -*- coding: utf-8 -*-
# time:2022/12/3 9:21
# file 倍数问题.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
n,k = map(int,input().split())
lists = list(map(int,input().split()))
lists.sort()
n = len(lists)

ans = 0
for i in range(n-2):
  for j in range(i+1,n-1):
    temp = lists[i] + lists[j] + lists[j+1]
    if temp % k == 0:
      ans = max(ans,temp)

print(ans)
