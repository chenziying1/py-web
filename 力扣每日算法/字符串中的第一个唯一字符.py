# -*- coding: utf-8 -*-
# time:2022/11/23 15:11
# file 字符串中的第一个唯一字符.py
# outhor:czy
# email:1060324818@qq.com


'''
字符串中的第一个唯一字符
给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

 

示例 1：

输入: s = "leetcode"
输出: 0
'''

#自己写的代码：用字典存放判断，用ans来存放单独的字符串存放的位置
class Solution:
    def firstUniqChar(self, s: str) -> int:
        target = {}
        for i in s:
            if i not in target:
                target[i] = 1
            else:
                target[i] += 1
        ans = -1
        for i in target:
            if target[i] == 1:
                if ans == -1:
                    ans = s.index(i)
                    if ans == 0:
                        return ans
                else:
                    if ans >= s.index(i):
                        ans = s.index(i)
        return ans



