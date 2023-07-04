from atexit import register
from random import randrange
from threading import BoundedSemaphore,Lock,Thread
from time import sleep,ctime

lock = Lock()
candytray = BoundedSemaphore(5)

def buy():
          lock.acquire()
          print('购买糖果...',end=' ')
          if candytray.acquire(False):
                    print('成功购买糖果')
          else:
                    print('糖果机为空，无法购买糖果')
          lock.release()

def refill():
          lock.acquire()
          print('重新添加糖果...',end=' ')
          try:
                    candytray.release()
          except ValueError:
                    print('糖果机都满了，无法添加')
          else:
                    print('成功添加糖果')
          lock.release()

def consumer(loops):
          for i in range(loops):
                    buy()
                    sleep(randrange(3))
def poducer(loops):
          for i in range(loops):
                    refill()
                    sleep(randrange(3))

def main():
          print('开始:',ctime())
          nloops = randrange(2,6)
          print('糖果机共有5个槽')
          Thread(target = consumer,args = (randrange(nloops,nloops+7),)).start()
          Thread(target = poducer,args = (nloops,)).start()

@register
def exit():
          print('程序执行完毕：',ctime())

if __name__ == '__main__':
          main()
          
