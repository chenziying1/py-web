# -*- coding: utf-8 -*-
# time:2022/11/23 9:46
# file app.py
# outhor:czy
# email:1060324818@qq.com
from pprint import pprint

from flask import Flask,render_template,request,redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("we have a post!")

        #如果file不在请求里面，重定向到提交的页面
        if "file" not in request.files:
            return redirect(request.url)

        #如果提交的是空白文件
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            #初始化
            recognizer = sr.Recognizer()
            #将文件转化为sr模块可以理解的方式
            audiofile = sr.AudioFile(file)
            with audiofile as source:
                data = recognizer.record(source)

            text = recognizer.recognize_sphinx(data)
            # 使用Sphinx识别语音
            try:
                print("Sphinx识别结果为:"+text)
            except sr.UnknownValueError:
                print("无法识别音频")
            except sr.RequestError as e:
                print("识别错误; {0}".format(e))
            transcript = text

    return render_template("index.html",transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True,threaded = True)