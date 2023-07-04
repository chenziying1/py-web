# -*- coding: utf-8 -*-
# time:2023/4/3 12:53
# file 瓶盖.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
n = eval(input())

ans = n

while n//3 != 0:
  ans += n//3
  n = n//3 + n%3

print(ans)