# -*- coding: utf-8 -*-
# time:2022/12/1 10:36
# file 合并两个有序数组.py
# outhor:czy
# email:1060324818@qq.com
from typing import List


def jiejue(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    end = m + n - 1
    while (j >= 0):
        if i >= 0 and (nums1[i] > nums2[j]):
            nums1[end] = nums1[i]
            end -= 1
            i -= 1
        else:
            nums1[end] = nums1[j]
            end -= 1
            j -= 1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n = len(nums1)
        n_nums2 = n - m
        for i in range(n_nums2):
            nums1[i+m] = nums2[i]
        nums1.sort()



jiejue([1,2,3,0,0,0], 3, [2,5,6], 3)