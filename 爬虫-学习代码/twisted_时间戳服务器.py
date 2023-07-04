from twisted.internet import reactor,protocol
from time import ctime

port = 9876
class MyProtocol(protocol.Protocol):
          def connectionMade(self):
                    client = self.transport.getPeer().host
                    print('客户端',client,'已连接')
          def dataReceived(self,data):
                    self.transport.write(ctime().encode(encoding='utf-8')+b" "+data)

factory = protocol.Factory()
factory.protocol = MyProtocol
print('正在等待客户端连接')
reactor.listenTCP(port,factory)
reactor.run()
