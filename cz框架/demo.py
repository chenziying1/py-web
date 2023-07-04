# -*- coding: utf-8 -*-
# time:2023/4/18 16:16
# file demo.py
# outhor:czy
# email:1060324818@qq.com

from cz框架.cz import SYLFK, simple_template, redirect, render_json, render_file
from cz框架.cz.session import session
from cz框架.cz.view import Controller
from core.base_view import BaseView, SessionView
from core.database import dbconn

class Register(BaseView):
    def get(self, request):
        # 收到 GET 请求时通过模版返回一个注册页面
        return simple_template("layout.html", title="注册",
                message="输入注册用户名")

    def post(self, request):
        # 把用户提交的信息作为参数，
        # 执行 SQL 的 INSERT 语句把信息保存到数据库的表中
        # 这里就是 shiyanlou 数据库中的 user 表里
        sql = "INSERT INTO user(f_name) VALUE('{}')".format(request.form['user'])
        ret = dbconn.insert(sql)
        # 如果添加成功，则表示注册成功，重定向到登录页面
        if ret.success:
            return redirect("/login")
        else:
            # 添加失败的话，把错误信息返回方便调试
            return render_json(ret.to_dict())

class API(BaseView):
    def get(self, request):
        data = {
            'name': 'shiyanlou_001',
            'company': '实验楼',
            'department': '课程部'
        }

        return render_json(data)

#下载文件
class Download(BaseView):
    def get(self, request):
        return render_file("1.txt")


# 首页视图
class Index(SessionView):
    def get(self, request):
        # 获取当前会话中的 user 的值
        user = session.get_item(request, 'user')

        # 把 user 的值用模版引擎置换到页面中并返回
        return simple_template("frist.html", user=user, message="hello world!")

# 登录视图
class Login(BaseView):
    def get(self, request):
        # 从 GET 请求中获取 state 参数，如果不存在则返回用默认值 1
        state = request.args.get('state', "1")
        # 通过模版返回给用户一个登录页面
        # 当 state 不为 1 时，页面信息返回用户名错误或不存在
        message = '输入登录用户名' if state == '1' else '用户名不存在'
        return simple_template("layout.html", title="登录", message=message)

    def post(self, request):
        # 把用户提交的信息到数据库中进行查询
        sql = "SELECT * FROM user WHERE f_name = '{}'".format(
                request.form['user'])
        ret = dbconn.execute(sql)
        # 如果有匹配的结果，说明注册过，反之再次重定向回登录页面
        # 并附带 state=0 过去，通知页面提示登录错误信息
        if ret.rows == 1:
            # 如果有匹配，获取第一条数据的 f_name 字段作为用户名
            user = ret.get_first()['f_name']
            # 把用户名放到 Session 中
            session.push(request, 'user', user)
            # Session 已经可以验证通过，所以重定向到首页
            return redirect("/")
        return redirect("/login?state=0")


# 登出视图
class Logout(SessionView):
    def get(self, request):
        # 从当前会话中删除 user
        session.pop(request, 'user')

        # 返回登出成功提示和首页链接
        return redirect("/") # 重定向到首页


syl_url_map = [
    {
        'url': '/',
        'view': Index,
        'endpoint': 'index'
    },
    {
        'url': '/register',
        'view': Register,
        'endpoint': 'register'
    },
    {
        'url': '/login',
        'view': Login,
        'endpoint': 'python链接mysqldemo'
    },
    {
        'url': '/logout',
        'view': Logout,
        'endpoint': 'logout'
    }
]


app = SYLFK()

index_controller = Controller('index', syl_url_map)
app.load_controller(index_controller)

app.run()