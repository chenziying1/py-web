# -*- coding: utf-8 -*-
# time:2022/11/30 10:24
# file 人物相关性分析.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
k = int(input())
strs = input()

n = len(strs)
number1,number2 = [],[]
count1,count2 = 0,0

#判断是否是字母
def IsLetter(index):
  if(index < 0 or index >= n):
    return False
  charAt = strs[index]
  return (charAt >= 'a' and charAt <= 'z') or (charAt >= 'A' and charAt <= 'Z')

#从头到尾的遍历，将Alice和Bob有多长放进去
for x in range(n):
  if not IsLetter(x-1) and x+4 < n and not IsLetter(x+5) and strs[x:x+5] == "Alice":
    number1.append(x)
    count1 += 1

  if not IsLetter(x-1) and x+2 < n and not IsLetter(x+3) and strs[x:x+3] == "Bob":
    number2.append(x)
    count2 += 1

#循环判断两端看看在不在距离范围内
ans = 0
if count1 == 0 or count2 == 0:
  ans = 0
else:
  left,right = 0,-1
  for x in range(count1):
    while (right + 1 < count2 and number2[right+1] <= number1[x] + k + 5):
      right += 1
    while (number2[left] + 3 + k < number1[x]):
      left += 1
    ans += right-left+1

print(ans)




