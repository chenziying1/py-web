import base64
import pickle
from django.shortcuts import render

def index(request):
    return render(request,"login.html")

def jiami(request):
    if request.method == "POST":
        message = request.POST.get('title')
        if message != None:
            s = pickle.dumps(message)
            b = base64.b64encode(s)
            return render(request,"show_message.html",{"ans":str(b,'utf-8')})
    return render(request,"login.html")

def jiemi(request):
    if request.method == "POST":
        message = request.POST.get('title2')
        if message != None:
            s = base64.b64decode(message)
            s = pickle.loads(s)
            return render(request, "show_message.html", {"ans": s})
    return render(request, "login.html")