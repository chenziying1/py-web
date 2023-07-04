import random
import string
import time

from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
import os



def frist(request):
    return render(request,'frist.html')

def show_category(request):
    return render(request, 'demo.html')

#处理数据的函数
def chuli(form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    phone = form.cleaned_data['phone']
    message = form.cleaned_data['message']
    jiaoyubeijing = form.cleaned_data['jiaoyubeijing']
    gongzhuojingli = form.cleaned_data['gongzhuojingli']
    xiangmujingli = form.cleaned_data['xiangmujingli']
    jinengzhengshu = form.cleaned_data['jinengzhengshu']
    return name,email,phone,message,jiaoyubeijing,gongzhuojingli,xiangmujingli,jinengzhengshu

def fristcontact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name,email,phone,message,jiaoyubeijing,gongzhuojingli,xiangmujingli,jinengzhengshu = chuli(form)
            file = request.FILES.get('file')
            media_url = "media/static/images/"
            form = ContactForm()
            return render(request, 'frist.html', {'name': name,'email': email,'phone': phone,'message': message,'jiaoyubeijing': jiaoyubeijing,
                                           'gongzhuojingli': gongzhuojingli,'xiangmujingli': xiangmujingli,'jinengzhengshu': jinengzhengshu,
                                                  'file':file,'media_url':media_url})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def secondcontact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name,email,phone,message,jiaoyubeijing,gongzhuojingli,xiangmujingli,jinengzhengshu = chuli(form)
            file = request.FILES.get('file')
            media_url = "media/static/images/"
            form = ContactForm()
            return render(request, 'second.html', {'name': name,'email': email,'phone': phone,'message': message,'jiaoyubeijing': jiaoyubeijing,
                                           'gongzhuojingli': gongzhuojingli,'xiangmujingli': xiangmujingli,'jinengzhengshu': jinengzhengshu,
                                                  'file':file,'media_url':media_url})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def threecontact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name,email,phone,message,jiaoyubeijing,gongzhuojingli,xiangmujingli,jinengzhengshu = chuli(form)
            file = request.FILES.get('file')
            media_url = "media/static/images/"
            form = ContactForm()
            return render(request, 'three.html', {'name': name,'email': email,'phone': phone,'message': message,'jiaoyubeijing': jiaoyubeijing,
                                           'gongzhuojingli': gongzhuojingli,'xiangmujingli': xiangmujingli,'jinengzhengshu': jinengzhengshu,
                                                  'file':file,'media_url':media_url})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def save_page(request):
    if request.method == 'POST':
        # 获取HTML代码并保存为文件
        html_code = request.POST.get('html_code')
        timestamp = str(int(time.time()))  # 获取当前时间戳并转换为字符串
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))  # 随机生成8位由小写字母和数字组成的字符串
        file_name = timestamp + random_string  + ".html"
        with open(file_name, 'w') as f:
            f.write(html_code)
        # 返回文件名
        return HttpResponse(file_name)
    else:
        return render(request, 'save_page.html')


def view_page(request, file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r') as f:
        response = HttpResponse(f.read(), content_type='text/html')
        return response

def change_view(request):
    return render(request,"change_pdf.html")

