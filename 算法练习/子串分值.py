# -*- coding: utf-8 -*-
# time:2022/12/2 9:50
# file 子串分值.py
# outhor:czy
# email:1060324818@qq.com

'''
最后还是没能解决超时的问题
'''

import os
import sys

# 请在此输入您的代码

#生成子字符串
def restr(s):
    results = []
    # x + 1 表示子串的长度
    for x in range(len(s)):
        # i 表示滑窗长度
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    return results

#生成子列表
def liebiao(s):
    List = [[]]
    for i in range(len(s)):  # 定长
        for j in range(len(List)):  # 变长
            sub_List = List[j] + [s[i]]
            if sub_List not in s:
                List.append(sub_List)
    print(List)




s = input()

ans = 0
temp = restr(s)
print(temp)
for i in temp:
    sets = []
    for j in i:
        print(j)
        if j not in sets:
            sets.append(j)
        else:
            sets.remove(j)

    ans += len(sets)
    print(sets)
    print("--------------")
print(ans)
