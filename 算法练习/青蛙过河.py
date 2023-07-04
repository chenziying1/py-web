# -*- coding: utf-8 -*-
# time:2023/4/7 15:20
# file 青蛙过河.py
# outhor:czy
# email:1060324818@qq.com

n, x = list(map(int, input().split()))
H = [0, *list(map(int, input().split()))]  # 下标从1开始
Pre_Sum = [0] * (n)
for idx in range(1, n):  # 预处理前缀和
    Pre_Sum[idx] = Pre_Sum[idx - 1] + H[idx]


# 判定能力为y时，是否合法
def check(y):
    # 枚举所有长度为y的区间
    for l in range(1, n - y + 1):
        r = l + y - 1
        if Pre_Sum[r] - Pre_Sum[l - 1] < 2 * x:
            return False
    return True


# 二分答案
l, r = 1, n
ans = -1
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)