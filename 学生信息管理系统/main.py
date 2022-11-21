# -*- coding: utf-8 -*-
# time:2022/11/21 11:17
# file main.py
# outhor:czy
# email:1060324818@qq.com
from datetime import timedelta

from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

students = [{ 'name': '张三','chinese': '65','math': '65','english': '65'},
            { 'name': '李四', 'chinese': '65', 'math': '65', 'english': '65'},
            {'name' : '王五', 'chinese': '65', 'math': '65', 'english': '65'},
            { 'name' : '赵六', 'chinese': '65', 'math': '65','english': '65'}]
a = len(students)

app.secret_key = "czy"
#半永久会话,保持五天,也可以改成minutes=5，五分钟
app.permanent_session_lifetime = timedelta(days=5)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        session["username"] = username
        session["password"] = password
        # 半永久会话
        session.permanent = True
        # 显示已经登录成功
        flash("login successful!", "info")
        return redirect('/home')
    return render_template("login.html")

@app.route('/admin')
def admin():
    if "username" in session:
        return render_template("admin.html",students=students,a = a)
    else:
        flash("you are not login in!", "info")
        return render_template("login.html")

@app.route('/add',methods=["POST","GET"])
def add():
    if request.method == "POST" :
        username = request.form["username"]
        chinese = request.form["chinese"]
        math = request.form["math"]
        english = request.form["english"]

        dicts = {}
        dicts["name"] = username
        dicts["chinese"] = chinese
        dicts["math"] = math
        dicts["english"] = english

        students.append(dicts)
        return redirect("/admin")
    return render_template("add.html")


@app.route('/delete')
def delete_student():
    delete_name = request.args['name']
    for i in students:
        if i['name'] == delete_name:
            students.remove(i)
    return redirect("/admin")

@app.route('/change',methods=["POST","GET"])
def change_student():
    if request.method == "POST" and "username" in session:
        chage_name = request.form['username']
        for i in students:
            if i['name'] == chage_name:
                username = request.form["username"]
                chinese = request.form["chinese"]
                math = request.form["math"]
                english = request.form["english"]

                i["name"] = username
                i["chinese"] = chinese
                i["math"] = math
                i["english"] = english
        return redirect("/admin")
    elif request.method == "GET" and "username" in session:
        change_name = request.args['name']
        for i in students:
            if i['name'] == change_name:
                return render_template("chage.html", students=i)
    else:
        flash("you are not login in!", "info")
        return redirect("/login")


#清除会话，退出登录
@app.route("/logout")
def logout():
    # 页面间消息的传递
    flash(f"you have beign logged out！", "info")
    session.pop("username",None)
    session.pop("password", None)
    return redirect(url_for("login"))

#数据可视化
@app.route("/view")
def view():
    dicts = [0,0,0,0]
    for i in students:
        if int(i["chinese"]) < 60:
            dicts[3] += 1
        elif int(i["chinese"]) >= 60 and int(i["chinese"]) < 70:
            dicts[0] += 1
        elif int(i["chinese"]) >= 70 and int(i["chinese"]) < 90:
            dicts[1] += 1
        elif int(i["chinese"]) >= 90 and int(i["chinese"]) <= 100:
            dicts[2] += 1
    return render_template("view.html",stu=dicts)

if __name__ == '__main__':
    app.run(debug=True)