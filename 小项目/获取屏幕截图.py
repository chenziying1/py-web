import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
canvas1 = tk.Canvas(root,width = 300,height = 300)
canvas1.pack()

def takeshotpicture():
          myscreenshot = pyautogui.screenshot()
          save_path = asksaveasfilename()
          myscreenshot.save(save_path+"_screenshot.png")


myButton = tk.Button(text="Take Shotpicture",command=takeshotpicture,font=10)
canvas1.create_window(150,150,window=myButton)

tk.mainloop()
