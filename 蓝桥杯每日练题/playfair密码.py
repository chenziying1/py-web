# -*- coding: utf-8 -*-
# time:2022/11/29 14:30
# file playfair密码.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
keyword = input()
nums = input()

targets = [chr(ord('a') + i) for i in range(26)]

for i in keyword:
    targets.remove(i)
keyword = list(keyword) + targets

target = [["" for j in range(5)] for i in range(5)]

a = 0
for i in range(5):
    for j in range(5):
        target[i][j] = keyword[a]
        a += 1
print(target)

n = len(nums)
ans = ""
for i in range(0, n-1, 2):
    print(i)
    for j in range(5):

        if nums[i] in target[j]:
            A, B = target[j].index(nums[i]), j
            print(A,B)
        if nums[i + 1] in target[j]:
            C, D = target[j].index(nums[i + 1]), j
            print(C,D)

    if A == C:
        ans += nums[i+1]
        ans += nums[i]
        A, B, C, D = "None", "None", "None", "None"

    elif B == D :
        ans += nums[i + 1]
        ans += nums[i]
        A, B, C, D = "None", "None", "None", "None"

    elif A != "None" and D != "None" and C != "None" and B != "None":
        print(target[C][B],target[A][D])
        ans += target[B][C]
        ans += target[D][A]
        A,B,C,D = "None","None","None","None"

    else:
        ans += nums[i]
        ans += nums[i+1]
        A, B, C, D = "None", "None", "None", "None"



if n % 2 != 0:
    ans += nums[-1]

print(ans)





