# -*- coding: utf-8 -*-
# time:2022/11/19 9:16
# file 截止日期计算器.py
# outhor:czy
# email:1060324818@qq.com

#session作为会话保持用户信息，在页面间跳转
from flask import Flask,redirect,url_for,render_template,request,session,flash
#实现类似与cookie登录的效果
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "czy"
app.permanent_session_lifetime = timedelta(days=5)


text_data = []


@app.route('/',methods = ["POST","GET"])
def home():
    global text_data
    if request.method == "POST":
        user = request.form.get('nm')
        names = request.form.get('nc')
        qingchu = request.form.get('qingchu')
        temp = [user,names]
        text_data.append(temp)
        if qingchu:
            text_data = []
        return render_template("home.html",endtime = user,names = names,text_data=text_data)
    return render_template("home.html",endtime = "2023/1/15 00:00:00",names="")

@app.route('/login',methods = ["POST","GET"])
def login():
    #如果获取到是正确的提交信息，转入用户页面
    if request.method == "POST":
        #nm是form代码中获取输入值的提示框名称
        user = request.form["nm"]
        #session保存会话信息
        session["user"] = user
        #半永久会话
        session.permanent = True
        #显示已经登录成功
        flash("login successful!","info")
        return redirect(url_for("user"))
    else:
        #如果不是提交post登录请求，来判断一下是否已登录
        if "user" in session:
            flash("aready login in!", "info")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route('/user',methods = ["POST","GET"])
def user():
    #检查用户是否已登录,否，去登陆
    #这样会报错，因为实际上session内容是加密的，我们得解密
    #传递email值
    email = None
    if "user" in session:
        user = session['user']
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("email is saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html",email = email)
    else:
        flash("you are not login in!", "info")
        return render_template("login.html")

#清除会话，退出登录
@app.route("/logout")
def logout():
    # 页面间消息的传递
    flash(f"you have beign logged out！", "info")
    session.pop("user",None)
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/view")
def view():
    return render_template("view.html")

if __name__ == '__main__':
    app.run(port=8000,debug=True)

