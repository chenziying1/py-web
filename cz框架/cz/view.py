# -*- coding: utf-8 -*-
# time:2023/4/16 8:35
# file view.py
# outhor:czy
# email:1060324818@qq.com

class Controller:

    def __init__(self,name, url_map):
        self.name = name #映射器的名字
        self.url_map = url_map ## 存放映射关系的列表，列表中的元素是字典

class View:

    methods = [] # 支持的请求方式的列表
    methods_meta = {} # 请求方式与对应的方法的映射


    def dispatch_request(self, request, *args, **option):
        """视图处理函数调度入口，子类须定义此方法
        """
        raise NotImplementedError

    @classmethod
    def get_func(cls, name):
        """创建视图函数，参数 name 就是函数名
        """
        def func(*args, **kw):
            # 通过视图对象调用处理函数调度入口，返回视图处理结果
            return cls().dispatch_request(*args, **kw)

        # 为视图函数绑定属性
        func.__name__ = name
        func.__doc__ = cls.__doc__
        func.__module__ = cls.__module__
        func.methods = cls.methods

        return func