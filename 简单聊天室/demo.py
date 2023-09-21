import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.clients = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message.encode('utf-8'))

    def handle_client(self, client):
        nickname = client.recv(1024).decode('utf-8')
        self.clients.append(client)
        self.broadcast(f'{nickname} joined the chat room!\n')
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message:
                    self.broadcast(f'{nickname}: {message}')
                else:
                    client.close()
                    self.clients.remove(client)
                    self.broadcast(f'{nickname} left the chat room!\n')
                    break
            except:
                client.close()
                self.clients.remove(client)
                self.broadcast(f'{nickname} left the chat room!\n')
                break

    def run(self):
        print('Server running...\n')
        while True:
            client, address = self.sock.accept()
            print(f'Connected with {str(address)}')
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.start()

server = Server('', 8000)
server.run()
