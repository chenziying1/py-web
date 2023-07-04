# -*- coding: utf-8 -*-
# time:2023/4/19 10:06
# file 大胖子走迷宫.py
# outhor:czy
# email:1060324818@qq.com

dirs = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs():
    q = [[3,3,0]]
    while len(q) != 0:
        now = q.pop(0)
        if now[0] == n-2 and now[1] == n-2:
            return now[2] + 1
        q.append([now[0],now[1],now[2]+1])
        for i in range(4):
            tx,ty = now[0] + dirs[i][0],now[1]+dirs[i][1]
            if now[2] >= 2*k:
                fat = 0
            else:
                if now[2] >= k:
                    fat = 1
                else:
                    fat = 2
            if (tx - fat < 1 or ty - fat < 1 or tx + fat > n or ty + fat > n):
                continue
            if (a[tx][ty] == '*'):
                continue
            if (vis[tx][ty]):
                continue
            ok = True
            if fat :
                for i in range(now[0]-fat,now[0]+fat+1):
                    for j in range(now[1]-fat,now[1]+fat+1):
                        if a[i][j] == '*' or i < 1 or i > n or j < 1 or j > n:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
            vis[tx][ty] = 1
            q.append([tx, ty, now[2] + 1])
    return -1




n,k = map(int,input().split())
vis=[[0 for i in range(n+k)] for j in range(n+k)]
a = [[0]*n]
for i in range(n):
    a.append([0] + list(input()))
vis[3][3] = 1;
print(bfs())