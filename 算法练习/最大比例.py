# -*- coding: utf-8 -*-
# time:2023/4/6 14:22
# file 最大比例.py
# outhor:czy
# email:1060324818@qq.com

n = int(input())
target = list(map(int,input().split()))
target = sorted(target)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

data = []
for i in range(n-1):
    if target[i+1] != target[i]:
        number = gcd(target[i+1],target[i])
        data.append([target[i+1]//number,target[i]//number])
data.sort()

print("%d/%d"%(data[0][0],data[0][1]))






