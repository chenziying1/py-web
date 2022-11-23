# -*- coding: utf-8 -*-
# time:2022/11/23 14:21
# file 反转字符串.py
# outhor:czy
# email:1060324818@qq.com

'''
反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
示例 1：
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
'''

#自己写的代码:其实用reverse一行解决，但还是用交换的方法解决了这个问题
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i],s[n-i-1] = s[n-i-1],s[i]