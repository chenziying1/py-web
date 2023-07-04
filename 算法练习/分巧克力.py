# -*- coding: utf-8 -*-
# time:2023/4/3 13:41
# file 分巧克力.py
# outhor:czy
# email:1060324818@qq.com

n,k = map(int,input().split())
a,b = [],[]
for i in range(n):
  target_a,target_b = map(int,input().split())
  a.append(target_a)
  b.append(target_b)


l,r = 1,100001
while l <= r:
    mid,ans = (l+r)//2,0
    cnt = 0
    for j in range(n):
        cnt += (a[j] // mid) * (b[j] // mid)
    if cnt >= k:
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans)

