# -*- coding: utf-8 -*-
# time:2022/11/26 15:53
# file 验证二叉搜索树.py
# outhor:czy
# email:1060324818@qq.com
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn08xg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#
# 验证二叉搜索树
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1：
# 输入：root = [2,1,3]
# 输出：true

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.panduan(self,root,-9223372036854775808,9223372036854775807)
    def isValidBST(self,root,test_Min,test_Max):
        if(root == None):
            return True
        if root.val >= test_Max or root.isValidBST() <= test_Min:
            return False
        # // 这里再分别以左右两个子节点分别判断，
        # // 左子树范围的最小值是minVal，最大值是当前节点的值，也就是root的值，因为左子树的值要比当前节点小
        # // 右子数范围的最大值是maxVal，最小值是当前节点的值，也就是root的值，因为右子树的值要比当前节点大
        return self.isValidBST(root.left, test_Min, root.val) and self.isValidBST(root.right, root.val, test_Max);


