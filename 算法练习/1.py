s = "yo|uar|e**|b|e***au|tifu|l"
ans = 0
flag = 0
if '*' not in s:
          print(0)
for i in s:
          #print(i)
          if flag == 2 and i == '*':
                ans += 1
          elif flag == 2 and i == '|':
                flag = 1
          elif i == '|':
                flag += 1
print(ans)
