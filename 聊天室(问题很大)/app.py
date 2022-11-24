# -*- coding: utf-8 -*-
# time:2022/11/24 10:10
# file app.py
# outhor:czy
# email:1060324818@qq.com

from flask import Flask,render_template,request,redirect,url_for
from flask_socketio import SocketIO,join_room

app = Flask(__name__)
#构建SocketIO
socketIO = SocketIO(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')
    if username and room:
        return render_template('chat.html',username=username,room=room)
    else:
        return redirect(url_for('home'))

@socketIO.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'],data['room']))
    join_room(data['room'])
    socketIO.emit("join_room_annoucentment",data)

@socketIO.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has send messgage to the room {}:{}".format(data['username'],data['room'],data['message']))
    socketIO.emit('receive_message', data,room = data['room'])

if __name__ == '__main__':
    socketIO.run(app,debug=True)