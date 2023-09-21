import random
from django.shortcuts import render
from django.views import View

def change(request):
    number = ['桐人', '亚诗娜', '诗乃']
    txt = random.choice(number)
    context_dict = {'boldmessage': txt}
    return render(request, 'login.html', context=context_dict)

def index(request):
    return render(request, 'login.html')