import pyautogui
import time
import random

#获取当前位置
curr_cords = pyautogui.position()
#记录离开键盘的时间
afk_counter = 0
while True:
          #如果停留时间超过指定时间，计数器增加，大于五后开始自由移动
          if pyautogui.position() == curr_cords:
                    afk_counter += 1
          else:
                    afk_counter = 0
                    curr_cords = pyautogui.position()
          if afk_counter > 5:
                    x = random.randint(1,1920)
                    y = random.randint(1,920)
                    pyautogui.moveTo(x,y,0.5)
                    curr_cords = pyautogui.position()
          print(f'AFK cOUNTER:{afk_counter}')
          time.sleep(2)
                    
          
