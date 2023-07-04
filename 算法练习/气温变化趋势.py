# -*- coding: utf-8 -*-
# time:2023/4/17 11:00
# file 气温变化趋势.py
# outhor:czy
# email:1060324818@qq.com

temperatureA = [21,18,18,18,31]
temperatureB = [34,32,16,16,17]

cnt, ans = 0, []
for i in range(len(temperatureA) - 1):
    if temperatureA[i + 1] > temperatureA[i] and \
            temperatureB[i + 1] > temperatureB[i]:
        cnt += 1

    elif temperatureA[i + 1] == temperatureA[i] and \
            temperatureB[i + 1] == temperatureB[i]:
        cnt += 1

    elif temperatureA[i + 1] < temperatureA[i] and \
            temperatureB[i + 1] < temperatureB[i]:
        cnt += 1

    else:
        ans.append(cnt)
        cnt = 0
print(ans)
print(max(max(ans),cnt))