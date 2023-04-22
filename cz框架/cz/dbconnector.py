# -*- coding: utf-8 -*-
# time:2023/4/16 8:33
# file dbconnector.py
# outhor:czy
# email:1060324818@qq.com

import pymysql

class BaseDB: #数据库客户端类，该类的实例即为连接数据库的对象

    def __init__(self,user, password, database='', host='127.0.0.1', \
                 port=3306, charset='utf8', cursor_class=pymysql.cursors.DictCursor):

        self.user = user # 用户名
        self.password = password # 密码
        self.database = database # 数据库
        self.host = host # 主机名，默认 127.0.0.1
        self.port = port # 端口号，默认 3306
        self.charset = charset # 数据库编码，默认 UTF-8
        self.cursor_class = cursor_class  # 数据库游标类型，默认为 DictCursor，返回的每一行数据集都是个字典
        self.conn = self.connect() # 数据库连接对象

    def connect(self): #数据库连接
        return pymysql.connect(host = self.host,user = self.user,port=self.port,password = self.password,\
                               db = self.database, charset=self.charset,cursorclass=self.cursor_class) #创建一个数据库连接对象并返回

    def close(self): #数据库关闭
        self.conn.close() #断开与数据库的连接

    def execute(self,sql,params = None): #执行sql语句
        """执行 SQL 语句并返回 DBResult 类的实例
                :param sql: SQL 语句字符串
                :param params: 字典对象 TODO
        """
        # 获取数据库连接对象的游标，这是一个上下文对象
        with self.conn.cursor() as cursor:
            # 如果参数是字典类型，将其和 SQL 语句一起传入 execute 方法
            # 反之只使用 SQL 语句调用 execute 方法
            # 执行结果为涉及的数据的行数，将其赋值给变量 rows
            rows = (cursor.execute(sql, params) if isinstance(params, dict)
                    else cursor.execute(sql))
            # 获取执行结果
            result = cursor.fetchall()
            self.conn.commit()
        # 返回影响条目数量和执行结果
        return rows, result

    def insert(self,sql,params = None): #插入数据
        # 获取 SQL 语句执行之后的 DBResult 对象
        ret = self.execute(sql, params)
        # 为 DBResult 对象的 result 属性重新赋值为插入数据的 ID
        ret.result = self.conn.insert_id()
        # 返回 DBResult 对象
        return ret

    # 存储过程调用
    def process(self, func, params=None):
        # 获取数据库连接对象的游标，这是一个上下文对象
        with self.conn.cursor() as cursor:
            # 如果参数是 Dict 类型，将其和 SQL 语句一起传入 callproc 方法
            # 反之只使用 SQL 语句调用 callproc 方法
            # 执行结果为涉及的数据的行数，将其赋值给变量 rows
            rows = (cursor.callproc(func, params) if isinstance(params, dict)
                    else cursor.callproc(func))
            # 获取存储过程执行结果
            result = cursor.fetchall()
            self.conn.commit()
        return rows, result

    # 创建数据库
    def create_db(self, db_name, db_charset='utf8'):
        """创建数据库"""
        sql = 'CREATE SCHEMA {} CHARSET {}'.format(db_name, db_charset)
        return self.execute(sql)

    # 删除数据库
    def drop_db(self, db_name):
        """删除数据库"""
        return self.execute('DROP DATABASE {}'.format(db_name))

    # 选择数据库
    def choose_db(self, db_name):
        """选择数据库"""
        # 调用 PyMySQL 的 select_db 方法选择数据库
        self.conn.select_db(db_name)
        # 因为正确执行的话没有影响条数和执行结果，所以返回两个空值 None
        return None, None





class DBResult:

    success = False # 执行成功与否
    result = None # 执行结果，通常是查询结果集，一个列表嵌套字典的结构
    error_info = None # 异常信息
    rows = None # 影响行数

    def index_of(self,index): #返回结果集合中指定索引的一条数据
        if (self.success and isinstance(index,int) and self.rows > index >= 0):
            return self.rows[index]

    def get_first(self): #返回结果集中的第一条数据
        return self.index_of(0)

    def get_last(self): #返回结果集中的最后条数据
        return self.index_of(-1)

    @staticmethod
    def handler(func): #捕获操作数据库时触发的异常的装饰器

        def decorator(*args, **options):
            ret = DBResult()
            try:
                ret.rows, ret.result = func(*args, **options) # 为 DBResult 实例的 rows 和 result 属性赋值
                ret.success = True  # 修改执行状态为 True 表示成功
            except Exception as e: # 如果捕获到异常，将异常放进 DBResult 对象的 error_info 属性中
                ret.error_info = e
            return ret # 返回 DBResult 实例

        return decorator

    def to_dict(self):
        """返回四个基本属性构成的字典对象
        """
        return {
            'success': self.success,
            'result': self.result,
            'error_info': str(self.error_info),
            'rows': self.rows
        }

