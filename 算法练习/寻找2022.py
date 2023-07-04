# -*- coding: utf-8 -*-
# time:2023/4/7 11:46
# file 寻找2022.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

N = 300
maps = [list(str(input())) for _ in range(N)]
length = 0
for i in range(N):
    for j in range(N):
        if maps[i][j] == '2':
            # 判断同行连续函数
            if j <= N - 4 and maps[i][j + 1] == '0' and maps[i][j + 2] == '2' and maps[i][j + 3] == '0':
                length += 1

            # 判断同列连续函数
            if i <= N - 4 and maps[i + 1][j] == '0' and maps[i + 2][j] == '2' and maps[i + 3][j] == '0':
                length += 1

            # 判断斜对角的连续函数
            if i <= N - 4 and j <= N - 4 and maps[i + 1][j + 1] == '0' and maps[i + 2][j + 2] == '2' and maps[i + 3][
                j + 3] == '0':
                length += 1
print(length)

