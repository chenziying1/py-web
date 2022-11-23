# -*- coding: utf-8 -*-
# time:2022/11/23 15:27
# file 有效的字母异位词.py
# outhor:czy
# email:1060324818@qq.com

'''
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。
示例1:
输入: s = "anagram", t = "nagaram"
输出: true
'''

#自己写的代码：
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        if s == t:
            return True
        else:
            return False