# -*- coding: utf-8 -*-
# time:2023/4/4 14:03
# file 工作区间.py
# outhor:czy
# email:1060324818@qq.com

n = 5
s = [1,2,4,6,8]
t = [3,5,7,9,10]
target = []
for i in range(len(s)):
    target.append([t[i],s[i]])
target.sort()
ans,t = 0,0
for i in target:
    if t<i[1]:
        ans += 1
        t = i[0]
print(ans)
