# -*- coding: utf-8 -*-
# time:2022/11/25 15:15
# file 删除链表中的节点.py
# outhor:czy
# email:1060324818@qq.com

'''
删除链表中的节点
有一个单链表的 head，我们想删除它其中的一个节点 node。
给你一个需要删除的节点 node 。你将 无法访问 第一个节点  head。
链表的所有值都是 唯一的，并且保证给定的节点 node 不是链表中的最后一个节点。
删除给定的节点。注意，删除节点并不是指从内存中删除它。这里的意思是：
给定节点的值不应该存在于链表中。
链表中的节点数应该减少 1。
node 前面的所有值顺序相同。
node 后面的所有值顺序相同。
自定义测试：
对于输入，你应该提供整个链表 head 和要给出的节点 node。node 不应该是链表的最后一个节点，而应该是链表中的一个实际节点。
我们将构建链表，并将节点传递给你的函数。
输出将是调用你函数后的整个链表。
'''

#自己写得代码：这里直接给出了要删除的节点，将要删除的节点指向下一个节点就可以了
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next