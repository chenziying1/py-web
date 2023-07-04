# -*- coding: utf-8 -*-
# time:2022/12/2 9:39
# file 天干地支.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
tiangan = ["geng","xin","ren","gui","jia","yi","bing","ding","wu","ji"]
dizhi = ["zi","chou","yin","mao","chen","si","wu","wei","shen","you","xu","hai"]

years = int(input())

temp = years-1900
if temp>0:
  print(tiangan[temp%10]+dizhi[temp%12])
else:
  print(tiangan[-(abs(temp)%10)]+dizhi[-(abs(temp)%12)])




