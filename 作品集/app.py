# -*- coding: utf-8 -*-
# time:2022/11/29 8:53
# file app.py
# outhor:czy
# email:1060324818@qq.com


from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)