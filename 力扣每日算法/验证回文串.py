# -*- coding: utf-8 -*-
# time:2022/11/24 15:11
# file 验证回文串.py
# outhor:czy
# email:1060324818@qq.com

'''
验证回文串
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
字母和数字都属于字母数字字符。
给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
示例 1：
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
'''

#自己写得代码：
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        target = ""
        for i in s:
            if i <= 'z' and i >= 'a' or (i <= '9' and i >= '0'):
                target += i
        if target == target[::-1]:
            return True
        else:
            return False

#参考其他人的代码：
    #双指针写法
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            if s == None or len(s) == 0:
                return True
            s = s.lower()
            i, j = 0, len(s) - 1
            while i < j:
                while i < j and not ((s[i] <= 'z' and s[i] >= 'a') or (s[i] <= '9' and s[i] >= '0')):
                    i += 1
                while i < j and not ((s[j] <= 'z' and s[j] >= 'a') or (s[j] <= '9' and s[j] >= '0')):
                    j -= 1
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True


