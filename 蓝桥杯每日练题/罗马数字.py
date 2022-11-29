# -*- coding: utf-8 -*-
# time:2022/11/29 13:40
# file 罗马数字.py
# outhor:czy
# email:1060324818@qq.com


import os
import sys

# 请在此输入您的代码
t = eval(input())

nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def chuli(target):
    target = target.upper()
    i, ans = len(target) - 1, 0
    while i >= 0 :
        if nums[target[i]] > nums[target[i - 1]] and i-1 >= 0:
            ans += nums[target[i]] - nums[target[i - 1]]
            i -= 2
        else:
            ans += nums[target[i]]
            i -= 1
    return ans


for i in range(t):
    target = input()
    ans = chuli(target)
    print(ans)
