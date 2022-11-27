# -*- coding: utf-8 -*-
# time:2022/11/26 15:33
# file 二叉树的最大深度.py
# outhor:czy
# email:1060324818@qq.com

# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnd69e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#
# 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       if root == None:
           return 0
       else:
           return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
       if root == None:
           return 0
       deque = []
       deque.append(root)
       count = 0
       while not (deque == []):
           size = len(deque)
           while size > 0:
               size -= 1
               cur = deque.pop();
               if (cur.left != None):
                   deque.append(cur.left)
               if (cur.right != None):
                   deque.append(cur.right)
           count += 1
       return count;




