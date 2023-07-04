# -*- coding: utf-8 -*-
# time:2023/4/5 14:23
# file 素数.py
# outhor:czy
# email:1060324818@qq.com

#判断是不是素数
def is_prime(n):
    for i in range(2,n):
        if i*i > n:
            break
        if n % i == 0:
            return False
    return n != 1

#判断一个区间内的有多少个素数
def sieve(n):
    is_prime2 = [True for i in range(n+1)]
    prime = [0 for i in range(n+1)]
    p = 0
    is_prime2[0] = is_prime2[1] = False
    for i in range(2,n+1):
        if is_prime2[i] == n:
            prime[p] = i
            p += 1
            for j in range(2*i,n+1,i):
                is_prime2[j] = False
    return p

#快速幂
def mod_pow(x,n,mod):
    res = 1
    while(n > 0):
        if (n & 1):
            res = res * x % mod
        x = x * x % mod
        n //= 2
    return res