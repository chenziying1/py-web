import _thread as thread
from time import sleep,ctime

def fun1():
          print('开始1',ctime())
          sleep(4)
          print('结束1',ctime())

def fun2():
          print('开始2',ctime())
          sleep(2)
          print('结束2',ctime())

def main():
          print('开始运行时间',ctime())
          thread.start_new_thread(fun1,())
          thread.start_new_thread(fun2,())
          sleep(6)
          print('结束时间',ctime())

main()
