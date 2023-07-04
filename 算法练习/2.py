grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]


for i in range(len(grid)):
          if grid[i][i] == 0 or grid[i][len(grid)-1-i] == 0:
                    print(False)

for i in range(len(grid)):
          for j in range(len(grid)):
                    if j == i or j == len(grid)-1-i:
                              continue
                    if grid[i][j] != 0:
                              print(False)

print(True)
