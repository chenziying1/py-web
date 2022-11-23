# -*- coding: utf-8 -*-
# time:2022/11/23 14:10
# file 旋转图像.py
# outhor:czy
# email:1060324818@qq.com

'''
旋转图像
给定一个 n×n 的二维矩阵matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
'''

#自己的代码：简单粗暴，我们会发现其实就是将第一列放到第一行，将第二列放到第二行
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        target = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                target[i][j] = matrix[n - j - 1][i]

        for i in range(n):
            matrix[i] = target[i]

#别人的代码：先上下交换，在对角线交换
#这样更慢了

def rotate(matrix):
    n = len(matrix)
    for i in range(n//2):
        matrix[i],matrix[n-i-1] = matrix[n-i-1],matrix[i]

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    return matrix

ans = rotate([[1,2,3],[4,5,6],[7,8,9]])
print(ans)

