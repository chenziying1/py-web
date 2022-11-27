import sys
import os

#s2.title()将单词首字母变成大写


target = input()
target_list = target.split(" ")

s1 = "".join(target_list)
s2 = " ".join(target_list)
daxie = "ASDFGHJKLZXCVBNMQWERTYUIOP"
xiaoxie = "asdfghjklzxcvbnmqwertyuiop"

def chuli():
    global n,daxie,xiaoxie
    for i in range(n):
        chuli = target_list.pop(0)

        start_num = chuli[0].upper()
        number = start_num + chuli[1:]
        m = len(number)

        for i in range(m - 1):

            if (number[i] in daxie or number[i] in xiaoxie) and (number[i + 1] >= '0' and number[i + 1] <= '9'):
                number = number[:i + 1] + '_' + number[i + 1:]

            elif (number[i + 1] in daxie or number[i + 1] in xiaoxie) and (number[i] >= '0' and number[i] <= '9'):
                number = number[:i + 1] + '_' + number[i + 1:]

        target_list.append(number)



if "" in target_list:
    print("")
elif s1.isalpha() or s1.isdigit():
    print(s2.title())
else:
    n = len(target_list)
    chuli()
    print(" ".join(target_list))




