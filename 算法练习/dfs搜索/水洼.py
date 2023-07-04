# -*- coding: utf-8 -*-
# time:2023/4/3 15:11
# file 水洼.py
# outhor:czy
# email:1060324818@qq.com

N,M = 10,12
s = [
    "w........ww.",
    ".www.....www",
    "....ww...ww.",
    ".........ww.",
    ".........w..",
    ".........w..",
    "..w.....ww..",
    "ww.w......w.",
    "..w.......w.",
    ".w.w......w.",
]

def dfs(x,y):
    s[x] = s[x][:y] + "." + s[x][y+1:]
    for dx in range(-1,2,1):
        for dy in range(-1,2,1):
            nx = x+dx
            ny = y+dy
            if(0<=nx and 0<= ny and nx < N and ny < M and s[nx][ny] == 'w'):
                dfs(nx,ny)

res = 0
for i in range(N):
    for j in range(M):
        if s[i][j] == 'w':
            dfs(i,j)
            res += 1
print(res)