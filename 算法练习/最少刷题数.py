# -*- coding: utf-8 -*-
# time:2023/4/7 17:33
# file 最少刷题数.py
# outhor:czy
# email:1060324818@qq.com

n = int(input())
a = [0] + list(map(int,input().split()))

cnt = [0 for i in range(max(a)+10)]
for i in range(1,n+1):
    cnt[a[i]] += 1
maxn = max(a)

for i in range(1,maxn+1):
    cnt[i] += cnt[i-1]

pos = -1
pos1 = -1

for i in range(1,maxn+1):
    if cnt[i-1] >= n -cnt[i]:
        if pos1 == -1:
            pos1 = i
    if cnt[i-1] - 1 >= n - cnt[i]:
        if pos == -1:
            pos = i
            break

ans = ""
if pos == -1:
    print("0 "*n)
else:
    for i in range(1,n+1):
        if a[i] >= pos1:
            ans += "0 "
        else:
            ans += str(pos - a[i]) + " "
    print(ans)
