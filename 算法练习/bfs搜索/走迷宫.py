# -*- coding: utf-8 -*-
# time:2023/4/3 16:25
# file 走迷宫.py
# outhor:czy
# email:1060324818@qq.com

import os
import sys

# 请在此输入您的代码
N,M = map(int,input().split())
target = []
for i in range(N):
  target.append(list(map(int,input().split())))
sx,sy,gx,gy = map(int,input().split())

d = [[10000 for i in range(N)] for j in range(M)]
d[sx-1][sy-1] = 0

dx,dy = [1,0,-1,0],[0,1,0,-1]
def bfs():
  que = [[sx-1,sy-1]]
  while len(que):
    q = que[0]
    que.pop(0)
    if q[0] == gx-1 and q[1] == gy-1:
      break
    for i in range(4):
      nx,ny = q[0]+dx[i],q[1]+dy[i]
      if (0 <= nx and 0 <= ny and nx < N and ny < M and d[nx][ny] == 10000 and target[nx][ny] == 1):
        que.append([nx,ny])
        d[nx][ny] = d[q[0]][q[1]] + 1


bfs()
print(d[gx-1][gy-1])

