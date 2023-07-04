# -*- coding: utf-8 -*-
# time:2022/11/27 15:14
# file 航行时间.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 本来以为是数学问题，结果只是两个数取平均值
t = eval(input())
qu, hui = [], []

def duqu():
    for i in range(t):
        qu_time = input().split(" ")
        qu.append(qu_time)
        hui_time = input().split(" ")
        hui.append(hui_time)

def chuli(libiao):
    day = 0
    for i in range(len(libiao)):

        start_time = list(map(int, libiao[0].split(":")))
        end_time = list(map(int, libiao[1].split(":")))

        h = (end_time[0] - start_time[0]) * 3600
        m = (end_time[1] - start_time[1]) * 60
        s = (end_time[2] - start_time[2])

        if len(libiao) == 3:
            day = int(libiao[2][1:-1])

        return (h + m + s + (day * 24 * 3600))


duqu()
for i in range(t):
    ans = (chuli(qu[i])+chuli(hui[i]))/2
    hh = int(ans / 3600)
    mm = int(ans / 60 % 60)
    ss = int(ans % 60)
    print('%02d:%02d:%02d' % (hh, mm, ss))



