from twisted.internet import reactor,protocol

host = 'localhost'
port = 9876

class MyProtocol(protocol.Protocol):
          def sendData(self):
                    data = input('>')
                    if data:
                              print('...正在发送 %s' % data)
                              self.transport.write(data.encode(encoding = 'utf-8'))
                    else:
                              self.transport.loseConnection()
          def connectionMade(self):
                    self.sendData()

          def dataReceived(self,data):
                    print(data.decode('utf-8'))
                    self.sendData()

class MyFactory(protocol.ClientFactory):
          protocol = MyProtocol
          clientConnectionLost = clientConnectionFailed = lambda self,connector,reason:reactor.stop()

reactor.connectTCP(host,port,MyFactory())
reactor.run()
