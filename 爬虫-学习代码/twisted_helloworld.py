
def hello():
          print("hello world!")
from twisted.internet import reactor
reactor.callWhenRunning(hello)
print("this is reactor")
reactor.run()
