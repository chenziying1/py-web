# -*- coding: utf-8 -*-
# time:2022/11/26 16:19
# file 单词分析.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码

#分析：单纯的排序问题
#sorted最好用，蓝桥杯系统sort识别不出来，sorted(ans.items(),key = lambda x:x[1],reverse = True)对字典排序
s = input()

ans = {}
for i in s:
  if i in ans:
    ans[i] += 1
  else:
    ans[i] = 1

sorts = sorted(ans.items(),key = lambda x:x[1],reverse = True)

target = [sorts[0][0]]
target_bijiao = sorts[0][1]
for i in sorts[1:]:
  if i[1] == target_bijiao:
    target.append(i[0])
  else:
    break

shuchu = sorted(target,reverse=False)
print(shuchu[0])
print(sorts[0][1])