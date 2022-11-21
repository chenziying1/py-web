# -*- coding: utf-8 -*-
# time:2022/11/21 11:17
# file main.py
# outhor:czy
# email:1060324818@qq.com


from flask import Flask,render_template,request,redirect

app = Flask(__name__)

students = [{ 'name': '张三','chinese': '65','math': '65','english': '65'},
            { 'name': '李四', 'chinese': '65', 'math': '65', 'english': '65'},
            {'name' : '王五', 'chinese': '65', 'math': '65', 'english': '65'},
            { 'name' : '赵六', 'chinese': '65', 'math': '65','english': '65'}]
a = len(students)


@app.route('/')
def home():
    return "<p>hello!</p>"

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return redirect('/admin')
    return render_template("login.html")

@app.route('/admin')
def admin():
    return render_template("admin.html",students=students,a = a)

@app.route('/add',methods=["POST","GET"])
def add():
    if request.method == "POST":
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
    if request.method == "POST":
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
    else:
        change_name = request.args['name']
        for i in students:
            if i['name'] == change_name:
                return render_template("chage.html", students=i)

if __name__ == '__main__':
    app.run(debug=True)