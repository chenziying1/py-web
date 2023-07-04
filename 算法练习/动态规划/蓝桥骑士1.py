# -*- coding: utf-8 -*-
# time:2023/4/5 13:51
# file 蓝桥骑士1.py
# outhor:czy
# email:1060324818@qq.com

def erfen(b,li):
    left,right = 0,len(b)-1
    while left <= right:
        mid = (left+right)//2
        if b[mid] > li:
            right = mid - 1
        elif b[mid] < li:
            left = mid + 1
        else:
            return left
    return left



N = int(input())
li = list(map(int, input().split()))
b = []
for i in range(N):
    if len(b) == 0 or li[i] > b[-1]:
        b.append(li[i])
    elif li[i] == b[-1]:
        continue
    else:
        col = erfen(b,li[i])
        b[col] = li[i]
print(len(b))
