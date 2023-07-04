# -*- coding: utf-8 -*-
# time:2023/4/22 10:06
# file 转换二维数组.py
# outhor:czy
# email:1060324818@qq.com
from collections import Counter

nums = [1,3,4,1,2,3,1]

ans = []
cnt = Counter(nums)
print(cnt)
while cnt:
    ans.append(list(cnt))
    print(ans)
    for x in ans[-1]:
        cnt[x] -= 1
        if cnt[x] == 0:
            del cnt[x]
print(ans)
