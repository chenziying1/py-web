# -*- coding: utf-8 -*-
# time:2023/4/7 9:54
# file 质因数.py
# outhor:czy
# email:1060324818@qq.com
k = int(input())

def sevive():
  is_prime = [True for i in range(1000)]
  is_prime[0] = is_prime[1] = False
  prime = []
  for i in range(2,1000):
    if is_prime[i]:
      prime.append(i)
      for j in range(2*i,1000,i):
        is_prime[j] = False
  return prime

prime_target = sevive()
ans = []
for i in prime_target:
  if k % i == 0:
    ans.append(i)
print(len(ans))


