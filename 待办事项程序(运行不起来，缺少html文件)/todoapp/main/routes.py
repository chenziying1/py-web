# -*- coding: utf-8 -*-
# time:2022/11/26 10:21
# file routes.py
# outhor:czy
# email:1060324818@qq.com
from flask import Blueprint,render_template

main = Blueprint('main',__name__)


@main.route('/')
def index():
    return render_template('index.html')