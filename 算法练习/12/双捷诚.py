import os
import sys

res = 1
# 请在此输入您的代码
for i in range(3, 2022, 2):
  res = res * i % 100000
print(res)