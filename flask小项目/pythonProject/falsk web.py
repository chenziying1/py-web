# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_mail import Mail, Message
from threading import Thread
import os

app = Flask(__name__)

mail = Mail(app)



@app.route('/send_email')
def send_email():
    msg.body = '内容'
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return 'success'


