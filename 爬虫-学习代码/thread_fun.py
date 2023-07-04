import random
from time import sleep,ctime
import threading

def fun(index,sec):
          print('开始:',index,'时间:',ctime())
          sleep(sec)
          print('结束:',index,'时间:',ctime())

def main():
          thread1 = threading.Thread(target = fun,args = (10,4))
          thread1.start()
          thread2 = threading.Thread(target = fun,args = (20,4))
          thread2.start()
          thread1.join()
          thread2.join()

main()
