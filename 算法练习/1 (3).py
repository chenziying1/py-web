n = 5
list1 = []
for i in range(n):
          row=[1]
          print(list1)
          list1.append(row)
          for m in range(1,i):
                    row.append(list1[i-1][m-1]+list1[i-1][m])
          row.append(1)
          for num in row:
                    print(num,end=" ")

