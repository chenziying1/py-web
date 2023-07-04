# -*- coding: utf-8 -*-
# time:2022/12/1 9:47
# file 日期问题.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
time = input().split("/")

ans = []


def paili():
    if int(time[0]) < 60:
        nums = "20" + str(time[0]) + "-" + str(time[1]) + "-" + str(time[2])
        if nums in ans:
            return
        else:
            ans.append(nums)
    else:
        nums = "19" + str(time[0]) + "-" + str(time[1]) + "-" + str(time[2])
        if nums in ans:
            return
        else:
            ans.append(nums)

    if int(time[2]) < 60:
        nums = "20" + str(time[2]) + "-" + str(time[1]) + "-" + str(time[0])
        if nums in ans:
            return
        else:
            ans.append(nums)
    else:
        nums = "19" + str(time[2]) + "-" + str(time[1]) + "-" + str(time[0])
        if nums in ans:
            return
        else:
            ans.append(nums)

    if int(time[2]) < 60:
        nums = "20" + str(time[2]) + "-" + str(time[0]) + "-" + str(time[1])
        if nums in ans:
            return
        else:
            ans.append(nums)

    else:
        nums = "19" + str(time[2]) + "-" + str(time[0]) + "-" + str(time[1])
        if nums in ans:
            return
        else:
            ans.append(nums)


def pandaun(x):
    target = list(map(int, x.split("-")))

    if (target[1] > 12 or target[1] <= 0) or (target[2] > 31 or target[2] <= 0):
        return False

    if target[1] in [4, 6, 9, 11]:
        if target[2] > 30:
            return False

    if target[1] == 2:
        if (target[0] % 4 == 0 and target[0] % 100 != 0) or (target[0] % 400 == 0):
            if target[2] > 29:
                return False
        else:
            if target[2] > 28:
                return False

    return True


paili()
ans = sorted(ans)
for i in ans:
    if pandaun(i):
        print(i)



#sorted是可以排列字符串的