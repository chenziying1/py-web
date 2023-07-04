import pyautogui
import time,random

output_list = ["你好","l am fine！"]

limits = int(input("No of messages: "))

for i in range(limits):
          output = ''.join(random.choice(output_list))
          time.sleep(1)
          pyautogui.typewrite(output)
          pyautogui.press("Enter")
          time.sleep(2)
