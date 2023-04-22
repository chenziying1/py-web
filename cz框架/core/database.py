# -*- coding: utf-8 -*-
# time:2023/4/22 10:45
# file database.py
# outhor:czy
# email:1060324818@qq.com

import sys
import os
from cz框架.cz.dbconnector import BaseDB

db_user = 'root'            # 连接用户名
db_password = os.environ.get('MYSQL_PWD') or ''    # 连接密码
db_database = "shiyanlou"   # 数据库库名

try:
    dbconn = BaseDB(db_user, db_password, db_database)
except Exception as e:
    code, _ = e.args

    # 如果异常代码为 1049 也就是数据库不存在异常，则开始创建
    # 反之为未知错误，输出信息并退出程序
    if code != 1049:
        print(e)
        exit()

    # 获取一个没有指定数据库的连接对象
    dbconn = BaseDB(db_user, db_password)

    # 创建数据库，返回一个 DBResult 对象
    ret = dbconn.create_db(db_database)

    # 定义创建数据表的语句
    create_table = '''
        CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            f_name VARCHAR(50) UNIQUE
        )'''

    # 如果创建数据库成功，切换到该数据库中
    if ret.success:
        ret = dbconn.choose_db(db_database)
        # 如果切换成功，开始创建数据表
        if ret.success:
            ret = dbconn.execute(create_table)

    # 如果以上步骤有任何一步出错，则删除数据库回退到创建数据库之前的状态
    if not ret.success:
        dbconn.drop_db(db_database)
        # 输出错误信息并退出
        print(ret.error_info)
        sys.exit()
