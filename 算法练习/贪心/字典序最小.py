# -*- coding: utf-8 -*-
# time:2023/4/4 14:44
# file 字典序最小.py
# outhor:czy
# email:1060324818@qq.com


s = "acdbcb"

a,b = 0,len(s)-1
t = ""
while a <= b:
    left = False
    for i in range(b):
        if a+i > b:
            break
        if s[a+i] < s[b-i]:
            left = True
            break
        if s[a+i] > s[b-i]:
            left = False
            break
    if left :
        t += s[a]
        a += 1
    else:
        t += s[b]
        b -= 1
print(t)