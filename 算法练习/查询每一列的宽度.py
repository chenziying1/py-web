# -*- coding: utf-8 -*-
# time:2023/4/18 11:07
# file 查询每一列的宽度.py
# outhor:czy
# email:1060324818@qq.com
grid = [[-15,1,3],[15,7,12],[5,6,-2]]

ans = []
for i in range(len(grid[0])):
    taregt = 0
    for j in range(len(grid)):
        print(i, j)
        if grid[j][i] or grid[j][i] == 0:
            temp = len(str(grid[j][i]))
            taregt = max(taregt, temp)
    ans.append(taregt)
print(ans)
