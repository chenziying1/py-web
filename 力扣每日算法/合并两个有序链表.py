# -*- coding: utf-8 -*-
# time:2022/11/25 15:45
# file 合并两个有序链表.py
# outhor:czy
# email:1060324818@qq.com

'''
合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：
输入：l1 = [], l2 = []
输出：[]
'''

#因为链表是升序的，我们只需要遍历每个链表的头，比较一下哪个小就把哪个链表的头拿出来放到新的链表中，
# 一直这样循环，直到有一个链表为空，然后我们再把另一个不为空的链表挂到新的链表中。
# 方法是对的，但不知道为什么放到力扣里行不通
# 现在改成递归
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None):
            return list2
        if(list2 == None):
            return list1

        dummy = ListNode(0)
        curr = dummy

        while (list1 != None and list2 != None):
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list2.next
            else:
                curr.next = list2
                list2 = list2.next

        curr = curr.next

        if list1 == None:
            curr.next = list2
        else:
            curr.next = list1

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if (list1.val < list2.val):
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2



