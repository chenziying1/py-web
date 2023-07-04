# -*- coding: utf-8 -*-
# time:2023/4/18 9:14
# file 迷宫2.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys
from queue import Queue
# 请在此输入您的代码
mp = []
for i in range(30):
  mp.append(input())
for i in range(len(mp)):
  mp[i] = '1' + mp[i] + '1'
mp = [52 * '1'] + mp + [52 * '1']
vis = [list(map(int,list(i))) for i in mp]
k = ('D','L','R','U')
dirs = ((1,0),(0,-1),(0,1),(-1,0))
vis[1][1] = 1
q = Queue()
q.put((1,1," "))
while q.qsize() != 0:
  now = q.get()
  if now[0] == 30 and now[1] == 50:
    print(now[2])
    exit
  for i in range(4):
    x = now[0] + dirs[i][0]
    y = now[1] + dirs[i][1]
    if vis[x][y] != 1:
      vis[x][y] = 1
      path = now[2]+k[i]
      q.put((x,y,path))
