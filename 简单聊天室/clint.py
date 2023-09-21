import tkinter as tk
import socket
import threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, message, nickname):
        message_with_nickname = f"{nickname}: {message}"
        self.sock.sendall(message_with_nickname.encode('utf-8'))

    def receive(self, chat_box):
        while True:
            message = self.sock.recv(1024)
            chat_box.insert(tk.END, message.decode('utf-8'))

    def close(self):
        self.sock.close()

    def run(self, chat_box, nickname):
        self.send(nickname, "") # 发送昵称
        receive_thread = threading.Thread(target=self.receive, args=(chat_box,))
        receive_thread.start()
        while True:
            message = self.message.get()
            self.send(message, nickname)
            self.message.set('')

# 创建Tkinter窗口
root = tk.Tk()
root.title('Chat Client')

# 添加窗口部件
message_frame = tk.Frame(root)
message_frame.pack()

scrollbar = tk.Scrollbar(message_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_box = tk.Listbox(message_frame, yscrollcommand=scrollbar.set)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=chat_box.yview)

message_entry = tk.Entry(root, width=60)
message_entry.pack(side=tk.LEFT, padx=5, pady=5)

send_button = tk.Button(root, text="Send", command=lambda: client.send(message_entry.get(), nickname.get()))
send_button.pack(side=tk.LEFT, padx=5, pady=5)

# 昵称输入框
nickname_label = tk.Label(root, text="Enter your nickname:")
nickname_label.pack()
nickname = tk.StringVar()
nickname.set('')
nickname_entry = tk.Entry(root, textvariable=nickname)
nickname_entry.pack()

# 启动客户端
client = Client('localhost', 8000)
client.message = tk.StringVar()
client.message.set('')
client.run_thread = threading.Thread(target=client.run, args=(chat_box, nickname.get()))
client.run_thread.start()

# 开始Tkinter事件循环
root.mainloop()

# 关闭客户端
client.close()