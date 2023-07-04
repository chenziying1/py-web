# -*- coding: utf-8 -*-
# time:2022/12/4 12:24
# file 奇怪的数列.py
# outhor:czy
# email:1060324818@qq.com

s = input()
n = int(input())


def fun(s):
    s2 = ''
    num = [i for i in s]
    while len(num) > 0:
        count = 0
        m = num[0]
        while m == num[0]:
            count += 1
            num.pop(0)
            if len(num) == 0:
                break
        s2 += str(count) + str(m)
    return s2


for j in range(n):
    s = fun(s)

print(s,end='')