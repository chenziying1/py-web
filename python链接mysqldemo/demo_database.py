# -*- coding: utf-8 -*-
# time:2023/5/1 13:24
# file demo_database.py
# outhor:czy
# email:1060324818@qq.com

#导入pymysql
#pip install pymssql 先安装

import pymssql #导入模块

connect = pymssql.connect('(local)','sa','123456','tushuguang')
#connect = pymssql.connect('服务器名称', '用户名', '密码', '库名')  # 建立连接
if connect:
    print("连接成功")
#输出
#连接成功

