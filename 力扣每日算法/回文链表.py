# -*- coding: utf-8 -*-
# time:2022/11/26 15:12
# file 回文链表.py
# outhor:czy
# email:1060324818@qq.com

'''
回文链表
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
示例 1：
输入：head = [1,2,2,1]
输出：true
示例 2：
输入：head = [1,2]
输出：false
'''

#1，反转后半部分链表这题是让判断链表是否是回文链表，
# 所谓的回文链表就是以链表中间为中心点两边对称。
# 我们常见的有判断一个字符串是否是回文字符串，这个比较简单，可以使用两个指针，一个最左边一个最右边，
# 两个指针同时往中间靠，判断所指的字符是否相等。
# 但这题判断的是链表，因为这里是单向链表，只能从前往后访问，
# 不能从后往前访问，所以使用判断字符串的那种方式是行不通的。
# 但我们可以通过找到链表的中间节点然后把链表后半部分反转（关于链表的反转可以看下432，剑指 Offer-反转链表的3种方式），
# 最后再用后半部分反转的链表和前半部分一个个比较即可。

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow = head,head
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        if (fast != None):
            slow = slow.next
        slow = self.reverses(slow)
        fast = head
        while (slow != None):
            if (fast.val != slow.val):
                return False
            fast = fast.next
            slow = slow.next
        return True


    def reverses(self,head):
        prev = None
        while (head != None):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

