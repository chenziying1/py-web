amount = [10,8,8]

n = amount.count(0)
ans = 0
if n >= 2:
          print(max(amount))
elif n == 1:
          amount.sort(reverse = True)
          temp = amount[0]-amount[1]
          ans += amount[1] + temp
          print(ans)
else:
          amount.sort(reverse = True)
          #print(amount)
          if amount[1] + amount[2] < amount[0]:
                    print(amount[1] + amount[2]+(amount[0]-amount[1] - amount[2]))
          elif amount[1] + amount[2] == amount[0]:
                    print(amount[0])
          else:
                    if amount[0] > 5:
                              ans1 = amount[0] - 5 + 1 +7
                              print(ans1)
                    if amount[0] <= 5:
                              print(7)
          
