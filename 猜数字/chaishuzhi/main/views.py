from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

import random
target = random.randint(1,100)
chishu = 5

def index(request):
    global chishu
    if request.method == "GET":
        global chishu
        chishu = 5
    if request.method == "POST":
        numbers = int(request.POST.get("title"))
        if chishu > 0:
            if numbers > target:
                text = "太大啦！"
            elif numbers < target:
                text = "太小啦！"
            else:
                text = "你猜对了！"
            chishu -= 1
        else:
            text = "你的次数已经用完啦!"
        content = {
            "text":text,
            "chishu":chishu
        }
        return render(request,"frist.html",context=content)
    return render(request,"frist.html",context={"chishu":5})


"""
这样不行，会出现由于url没改变导致每次点击提交按钮时都会重置到五

def genxing(request):
    global chishu
    chishu = 5
    return render(request,"frist.html",context={"chishu":5})
"""

def genxing(request):

    return render(request,"frist.html",context={"chishu":5})