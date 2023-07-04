# -*- coding: utf-8 -*-
# time:2023/6/15 16:47
# file demo.py
# outhor:czy
# email:1060324818@qq.com

import json
from flask import Flask,render_template,request,redirect
import find_target
import xiangsi
import daopaisuoyin

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():

    transcript,transcript2 = "",""
    if request.method == "POST":
        print("we have a post!")
        res = request.form.get('text')

        xiangsi.search_text = res
        ans = xiangsi.main()
        target = ""
        for i in ans:
            target += i +" "
        transcript = target

        daopaisuoyin.search_text = res
        ans = daopaisuoyin.search_data()
        target = ""
        for i in ans:
            target += i +" "
        print(target)
        transcript2 = target

    return render_template("frist.html",transcript=transcript,transcript2=transcript2)


if __name__ == "__main__":
    app.run(debug=True,threaded = True)