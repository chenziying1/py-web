# -*- coding: utf-8 -*-
# time:2023/4/7 12:00
# file fi集合.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码

a = [1,2,3]
count = 0
for i in a:

  if count < 5000:  # 搞一个比较大的范围，确保有2020个元素
    a.append(3 * i + 2)
    a.append(5 * i + 3)
    a.append(8 * i + 5)
    count += 1
  else:
    break
s = set(a)  # 去重
ans = sorted(s)  # 升序排列
print(ans[2018])  #
