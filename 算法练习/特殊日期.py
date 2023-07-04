# -*- coding: utf-8 -*-
# time:2023/4/7 7:50
# file 特殊日期.py
# outhor:czy
# email:1060324818@qq.com

day_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_D(number):
    month = number//100
    day = number%100

    if month < 1 or month > 12:
        return 0
    if day < 1 or day > day_per_month[month]:
        return 0
    return 1




def is_H(H):
    h = H // 100
    m = H % 100
    if h < 0 or h > 23:
        return 0
    if m < 0 or m > 59:
        return 0
    return 1


ans = 0
for a in range(10):
    for b in range(10):
        if a == b:
            continue

        Y,D,H = 4,0,0
        Y_number = [a,a,a,a]
        for i in range(4):
            Y_number[i] = b
            target = 0
            for j in Y_number:
                target = target*10+j
            D += is_D(target)
            H += is_H(target)
            Y_number[i] = a
        ans += Y*D*H
print(ans)
