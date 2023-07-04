# -*- coding: utf-8 -*-
# time:2022/11/20 15:50
# file second.py
# outhor:czy
# email:1060324818@qq.com


from flask import Blueprint, render_template

second = Blueprint("second",__name__,static_folder="static",template_folder="templates")


@second.route("/home")
@second.route("/")
def home():
    return render_template("home.html")
