# -*- coding: utf-8 -*-
# time:2023/4/18 10:27
# file 跳蚱蜢.py
# outhor:czy
# email:1060324818@qq.com

def insertQueue(q,dir,news,vis):
    pos = news[1]
    status = news[0]
    insertpos = (pos + dir + 9) % 9
    t = list(status)
    t[pos],t[insertpos] = t[insertpos],t[pos]
    addstatus = " ".join(t)
    if addstatus not in vis:
        vis.add(addstatus)
        q.append((addstatus,insertpos,news[2]+1))

q = [("012345678",0,0)]
vis = set()
vis.add("012345678")
while q:
    news = q.pop(0)
    if news[0] == "087654321":
        print(news[2])
        break
    insertQueue(q,-2,news,vis)
    insertQueue(q, -1, news, vis)
    insertQueue(q, 1, news, vis)
    insertQueue(q, 2, news, vis)
