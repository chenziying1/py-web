# -*- coding: utf-8 -*-
# time:2022/11/24 17:14
# file 最长公共前缀.py
# outhor:czy
# email:1060324818@qq.com

'''
最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        n = len(strs)
        for i in range(1,n):
            temp,target = "",strs[i]
            for j in range(len(target)):
                if j >= len(ans):
                    break
                elif ans[j] == target[j]:
                    temp += ans[j]
                    continue
                else:
                    break
            ans = temp
        return ans