import random
from time import sleep,ctime
import _thread as thread

def fun(index,sec,lock):
          print('开始',index,'时间:',ctime())
          sleep(sec)
          print('结束',index,'时间:',ctime())
          lock.release()

def main():
          lock1 = thread.allocate_lock()
          lock1.acquire()
          thread.start_new_thread(fun,(10,4,lock1))
          lock2 = thread.allocate_lock()
          lock2.acquire()
          thread.start_new_thread(fun,(20,2,lock2))
          while lock1.locked() or lock2.locked():
                    pass

main()
