# -*- coding: utf-8 -*-
# time:2022/11/25 15:36
# file 反转链表.py
# outhor:czy
# email:1060324818@qq.com
'''
反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：
输入：head = [1,2]
输出：[2,1]
示例 3：
输入：head = []
输出：[]
'''

#1，使用栈解决  链表的反转是老生常谈的一个问题了，同时也是面试中常考的一道题。
# 最简单的一种方式就是使用栈，因为栈是先进后出的。实现原理就是把链表节点一个个入栈，当
# 全部入栈完之后再一个个出栈，出栈的时候在把出栈的结点串成一个新的链表。
# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while (head != None):
            stack.append(head)
            head = head.next

        if(stack == []):
            return None

        #py.pop将列表最后一个元素弹出
        node = stack.pop()
        dummy = node

        while (stack != []):
            tempnode = stack.pop()
            node.next = tempnode
            node = node.next


        node.next = None
        return dummy