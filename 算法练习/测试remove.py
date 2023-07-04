a = [1,2,3,4]
for i in range(1,5):
          del a[i-1]
          print(a)
          print(a.index(i+1))
