# -*- coding: utf-8 -*-
# time:2023/4/6 10:42
# file 跳杯子.py
# outhor:czy
# email:1060324818@qq.com
import sys
from collections import deque  # BFS用deque实现

st=input() # 起始状态，字符串
ed=input() # 终止状态
all_st=set() # 记录所有状态的集合
q=deque()


skip=[1,-1,2,-2,3,-3]  # 6种合法跳跃情况，正数空杯往右跳，负数空杯往左挑
q.append([list(st),0])  # 起点入队，把（状态和步数）加进去。把状态转为列表，步数为0
all_st.add(st)  # 所有状态的集合中加入初始状态


while len(q):
    czt,cskip = q.popleft()
    for x in skip:
        lzt = czt.copy()
        p = lzt.index('*')
        next_p = p + x
        if 0 <= next_p < len(czt):
            lzt[p],lzt[next_p] = lzt[next_p],lzt[p]
            now_cskip = cskip + 1
            now_czt = "".join(lzt)
            if now_czt == ed:
                print(now_cskip)
                sys.exit()
            if now_czt not in all_st:
                all_st.add(now_czt)
                q.append([lzt, now_cskip])



