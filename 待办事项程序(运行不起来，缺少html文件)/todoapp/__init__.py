# -*- coding: utf-8 -*-
# time:2022/11/26 9:27
# file __init__.py
# outhor:czy
# email:1060324818@qq.com

from flask import Flask
from .extensions import mongo
from .main.routes import main

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = 'mongodb+srv://sa:123456@cluster0.qk9q28c.mongodb.net/mydb?retryWrites=true&w=majority'
    mongo.init_app(app)
    app.register_blueprint(main)
    return app

create_app()