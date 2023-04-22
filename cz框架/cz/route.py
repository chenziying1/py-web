# -*- coding: utf-8 -*-
# time:2023/4/16 8:34
# file route.py
# outhor:czy
# email:1060324818@qq.com

class Route:

    def __init__(self,app):
        self.app = app

    def __call__(self, url, **options):

        if 'methods' not in options: #如果参数中不含get，post这些请求
            options['methods'] = ['GET'] #初始化为仅支持get

        #封装一个函数，并且用这样或者那样的方式来修改它的行为
        def decorator(f):
            self.app.add_url_rule(url, f, 'route', **options)
            return f

        return decorator




