# -*- coding: utf-8 -*-
# time:2022/12/4 12:02
# file 拼接平方数.py
# outhor:czy
# email:1060324818@qq.com


import math


def is_pingfang(x):
  a = int(math.sqrt(x))
  return a*a==x


def check(n):
  s = str(n)
  for i in range(1, len(s)):
    s1 = s[0:i]
    s2 = s[i:]

    if is_pingfang(int(s1)) and is_pingfang(int(s2)) and int(s2) != 0:
      return True
  return False


a, b = map(int, input().split())
for i in range(a, b+1):
  if i ** 0.5 % 1 == 0:
    if check(i):
      print(i)
