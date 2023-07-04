# -*- coding: utf-8 -*-
# time:2022/11/19 9:16
# file 截止日期计算器.py
# outhor:czy
# email:1060324818@qq.com

#session作为会话保持用户信息，在页面间跳转
from flask import Flask,redirect,url_for,render_template,request,session,flash
#实现类似与cookie登录的效果
from datetime import timedelta
#数据库操作
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "czy"
#半永久会话,保持五天,也可以改成minutes=5，五分钟
app.permanent_session_lifetime = timedelta(days=5)
#数据库消息配置
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#创建数据库对象
db = SQLAlchemy(app)

#创建数据库模型
class users(db.Model):
    _id = db.Column("id",db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name,email):
        self.name = name
        self.email = email

@app.route('/')
def home():
    return render_template("home.html")

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

        #执行数据库语句
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user,"")
            db.session.add(usr)
            db.session.commit()

        #显示已经登录成功
        flash("login successful!","info")
        return redirect(url_for("user"))
    else:
        #如果不是提交post登录请求，来判断一下是否已登录
        if "user" in session:
            flash("aready login in!", "info")
            return redirect(url_for("user"))
        return render_template("layout.html")


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

            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("email is saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html",email = email)
    else:
        flash("you are not login in!", "info")
        return render_template("layout.html")

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
    return render_template("view.html",values=users.query.all())

if __name__ == '__main__':
    db.create_all()
    app.run(port=8000,debug=True)




'''
@app.route("/<name>")
def user(name):
    return "hello {}!".format(name)

@app.route('/admin/')
def admin():
    return redirect(url_for("user",name="Admin"))
'''