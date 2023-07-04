from tkinter import *
from time import strftime
from tkinter.ttk import *
import tkinter.font as tkFont


root = Tk()
root.title("CLOCK")

#显示时间
def time():
          strings = strftime("%H:%M:%S %p")
          label.config(text=strings)
          label.after(1000,time)

#winfo_screenwidth获取屏幕宽度
#winfo_screenheight获取屏幕高度
#字符串形式为"宽度x高度，geometry（）设置应用的大小
#attributes方法用于修改窗口属性。我们需要置顶窗口覆盖掉所有其他窗口，attributes方法中，置顶窗口的属性名为-topmost，其用法是attributes(属性名，属性值)我们加入代码win.attributes("-topmost",True)即可置顶窗口，实现真正的全屏。
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("%dx%d" %(w,h))
root.attributes("-topmost",True)

#设置背景颜色为黑
root.configure(bg = "black")

#设置标签居中
frame = Frame(root)

label = Label(frame,font=("ds-digital",80),background="black",foreground="cyan")
#默认值为center，所以不写也行
frame.pack(expand=True)
label.pack()
time()

root.mainloop()
