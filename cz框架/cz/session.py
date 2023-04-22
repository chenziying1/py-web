# -*- coding: utf-8 -*-
# time:2023/4/16 8:34
# file session.py
# outhor:czy
# email:1060324818@qq.com

import base64
import json
import os
import time

def create_session_id():
    return base64.encodebytes(str(time.time()).encode()).decode()[:-2][::-1] #主要就是生成一串毫无意义的字符串当作id，这里利用了时间

def get_session_id(request): #从请求中获取 Session ID
    return request.cookies.get('session_id', '')

class Session:

    def __init__(self,session_path='session'):
        self.__session_map__ = {} # 会话映射表
        self.__storage_path__ = session_path  # 会话本地存放目录
        if not os.path.exists(self.__storage_path__): #如果本地存放目录不存在，则创建
            os.makedirs(self.__storage_path__)


    def __new__(cls, *args, **kw):
        """单例模式，实现一个全局 Session 类的实例
        """
        if not hasattr(cls, '_Session__instance'):
            cls.__instance = super().__new__(cls, *args, **kw)
        return cls.__instance

    def push(self, request, item, value):
        """更新或添加会话
        """
        session_id = get_session_id(request) # 从请求中获取客户端的 Session ID
        if session_id in self.__session_map__:
            self.__session_map__[session_id][item] = value
        else:
            self.__session_map__[session_id] = {item: value}

    def pop(self, request, item, value=True):
        """删除当前会话的某个字段
        """
        session_id = get_session_id(request) # 从请求中获取客户端的 Session ID
        current_session = self.__session_map__.get(session_id, {})
        if item in current_session:
            current_session.pop(item)

    def set_storage_path(self, session_path): #修改存放的目录
        self.__storage_path__ = session_path
        if not os.path.exists(self.__storage_path__):
            os.makedirs(self.__storage_path__)

    def storage(self, session_id): #会话持久化
        filename = os.path.join(self.__storage_path__, session_id)
        with open(filename, 'wb') as f:
            content = json.dumps(self.__session_map__.get(session_id))
            f.write(base64.encodebytes(content.encode()))

    def load_all_session(self):
        """加载本地文件中的会话数据
        """
        session_file_list = os.listdir(self.__storage_path__)

        for session_id in session_file_list:
            path = os.path.join(self.__storage_path__, session_id)
            with open(path, 'rb') as f:
                content = f.read()
            # 把文件内容进行 base64 解码
            content = base64.decodebytes(content)
            # 把 Session ID 于对应的会话内容绑定添加到会话映射表中
            self.__session_map__[session_id] = json.loads(content.decode())

    def get(self, request):
        """获取当前请求相关会话数据
        """
        return self.__session_map__.get(get_session_id(request), {})

    # 获取当前会话的某个项
    def get_item(self, request, item):
        """获取当前请求相关会话数据中的某个字段
        """
        return self.get(request).get(item, None)


class AuthSession:
    """Session 校验基类
    """

    @classmethod
    def auth_session(cls, f, *args, **options):
        """Session 校验装饰器
        """
        def decorator(obj, request):
            if cls.auth_logic(request, *args, **options):
                return f(obj, request)
            return cls.auth_fail_callback(request, *args, **options)
        return decorator

    # 验证逻辑的接口，返回一个布尔值
    @staticmethod
    def auth_logic(request, *args, **options):
        raise NotImplementedError

    # 验证失败的回调接口
    @staticmethod
    def auth_fail_callback(request, *args, **options):
        raise NotImplementedError

session = Session()