# -*- coding: utf-8 -*-
# time:2023/4/19 14:09
# file base_view.py
# outhor:czy
# email:1060324818@qq.com
from cz框架.cz import redirect
from cz框架.cz.view import View
from cz框架.cz.session import AuthSession, session

class BaseView(View):
    # 定义支持的请求方法，默认支持 GET 和 POST 方法
    methods = ['GET', 'POST']

    # POST 请求处理函数
    def post(self, request, *args, **options):
        pass

    # GET 请求处理函数
    def get(self, request, *args, **options):
        pass

    # 视图处理函数调度入口
    def dispatch_request(self, request, *args, **options):
        """处理请求的核心函数，该函数会被视图函数调用
        """
        if request.method in self.methods:
            func = getattr(self, request.method.lower())
            return func(request, *args, **options)
        return '<h1>Unknown or unsupported require method.</h1>'

# 登录验证类
class AuthLogin(AuthSession):

    # 如果没有验证通过，则返回一个链接点击到登录页面
    @staticmethod
    def auth_fail_callback(request, *args, **options):
        return redirect("/login") #重定向返回

    # 验证逻辑，如果 user 这个键不在会话当中，则验证失败，反之则成功
    @staticmethod
    def auth_logic(request, *args, **options):
        if 'user' in session.get(request):
            return True
        return False


# 会话视图基类
class SessionView(BaseView):

    # 验证类抓装饰器
    @AuthLogin.auth_session
    def dispatch_request(self, request, *args, **options):
        # 结合装饰器内部的逻辑，调用继承的子类的 dispatch_request 方法
        return super(SessionView, self).dispatch_request(request, *args, **options)