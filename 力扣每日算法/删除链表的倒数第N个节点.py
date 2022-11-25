# -*- coding: utf-8 -*-
# time:2022/11/25 15:19
# file 删除链表的倒数第N个节点.py
# outhor:czy
# email:1060324818@qq.com
'''
删除链表的倒数第N个节点
给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。
示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：
输入：head = [1], n = 1
输出：[]
示例 3：
输入：head = [1,2], n = 1
输出：[1]
'''

#非递归解决这题让删除链表的倒数第n个节点，首先最容易想到的就是先求出链表的长度length，
#然后就可以找到要删除链表的前一个结点，让他的前一个结点指向要删除结点的下一个结点即可
#看得出来力扣使用链表进行1.遍历的方法2.删除的方法3.取节点的值
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class test:
    def removeNthFromEnd(head, n, self):
        pre = head
        last = self.length(head)-n
        if (last == 0):
            return head.next
        for i in range(last-1):
            pre = pre.next
        pre.next = pre.next.next
        return head

    def length(self,head):
        len = 0
        while (head != None):
            len += 1
            head = head.next
        return len


