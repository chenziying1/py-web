# -*- coding: utf-8 -*-
# time:2023/4/17 10:25
# file 寒假作业.py
# outhor:czy
# email:1060324818@qq.com


import os
import sys

# 请在此输入您的代码
ans = 0
b = [0 for _ in range(15)]
vis = [0 for _ in range(15)]


def check3(): return b[1] + b[2] == b[3]


def check6(): return b[4] - b[5] == b[6]


def check9(): return b[7] * b[8] == b[9]


def check12(): return b[10] == b[11] * b[12]


def dfs(num):
    global ans
    if num == 13:
        if check12(): ans += 1
        return
    if num == 4 and not check3(): return
    if num == 7 and not check6(): return
    if num == 12 and not check9(): return
    for i in range(1, 14):
        if not vis[i]:
            b[num] = i
            vis[i] = 1
            dfs(num + 1)
            vis[i] = 0


dfs(1)
print(ans)


