# -*- coding: utf-8 -*-
# time:2023/4/3 15:38
# file 迷宫.py
# outhor:czy
# email:1060324818@qq.com

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M=10,10
s = [
    "#s######.#",
    "......#..#",
    ".#.##.##.#",
    ".#........",
    "##.##.####",
    "....#....#",
    ".#######.#",
    "....#.....",
    ".####.###.",
    "....#...G#",
]
sx,sy = 0,1
gx,gy = 9,8
def bfs():
    que = []
    d = [[10000 for i in range(N)] for j in range(M)]
    que.append([sx,sy])
    d[sx][sy] = 0
    while(len(que)):
        p = que[0]
        que.pop(0)
        if p[0]== 9 and p[1] == 8:
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if (0 <= nx and 0 <= ny and nx < N and ny < M and s[nx][ny] != '#' and d[nx][ny] == 10000):
                que.append([nx,ny])
                d[nx][ny] = d[p[0]][p[1]] + 1
    return d[gx][gy]

res = bfs()
print(res)
