# -*- coding: utf-8 -*-
# time:2022/11/26 16:49
# file 删除字符.py
# outhor:czy
# email:1060324818@qq.com

# 题目描述
# 给定一个单词，请问在单词中删除 tt 个字母后，能得到的字典序最小的单词是什么？
#
# 输入描述
# 输入的第一行包含一个单词，由大写英文字母组成。
# 第二行包含一个正整数 tt。
# 其中，单词长度不超过 100100，tt 小于单词长度。
#
# 输出描述
# 输出一个单词，表示答案。

# 输入输出样例
# 示例 1
# 输入
# LANQIAO
# 3
# 输出
# AIAO

#解题：第一遍看的时候还以为是按照大小删除字符，留下了的就是答案
#这个想法是错误的，应该是一个字符一个字符的对比过去，大的就删掉，小的留下
#知识点：remove（）用法，list可以直接变字符串为列表，列表不能直接变字符串

import os
import sys

# 请在此输入您的代码
target = input()
t = eval(input())

list_target = list(target)

for i in range(t):
  if list_target[1] < list_target[0]:
    list_target.remove(list_target[0])
  else:
    list_target.remove(list_target[1])

ans =""
for i in list_target:
  ans += i

print(ans)
