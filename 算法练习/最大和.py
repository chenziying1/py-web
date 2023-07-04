# -*- coding: utf-8 -*-
# time:2023/4/7 10:10
# file 最大和.py
# outhor:czy
# email:1060324818@qq.com

def is_prime(x):
    for i in range(2,x):
        if i*i > x:
            break
        if x % i == 0:
            return False
    return x != 1

def min_prime(x):
    for i in range(2,x+1):
        sum = 0
        if (x % i == 0):
            for j in range(2,i+1):
                if i % j == 0:
                    sum += 1
            if sum == 1:
                return i



f = [-10000 for i in range(10001)]
n = int(input())
lists = [0]+list(map(int,input().split()))

f[1] = lists[1]

for i in range(1,n+1):
    d = min_prime(n-i)
    print(d)
    for j in range(i+1,i+d+1):
        f[j] = max(f[j],f[i]+lists[j])
print(f[n])
