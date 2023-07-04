# -*- coding: utf-8 -*-
# time:2023/4/6 16:32
# file 时间显示.py
# outhor:czy
# email:1060324818@qq.com
import time
n = int(input())//1000


print(time.asctime(time.gmtime(n))[11:-5])