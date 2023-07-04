# -*- coding: utf-8 -*-
# time:2022/11/21 9:16
# file route.py
# outhor:czy
# email:1060324818@qq.com

from app import app#从app包中导入 app这个实例

#2个路由
@app.route('/')
@app.route('/index')
#1个视图函数
def index():
	return "Hello,World!"#返回一个字符串
