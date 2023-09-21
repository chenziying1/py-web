from django.http import HttpResponse
from django.shortcuts import render
from .forms import xingxiForm
from .models import xingxi

def frist(request):
    return render(request,'login.html')

def show_category(request):
    category_list = xingxi.objects.filter(name="good")
    context_dict = {'categories': category_list}
    return render(request, 'demo.html', context_dict)

def add_category(request):
    form = xingxi()
    if request.method == 'POST':
        form = xingxiForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            field1_value = form.cleaned_data['name']
            category_list = xingxi.objects.filter(name=field1_value)
            context_dict = {'categories': category_list}
            return render(request, 'demo.html', context_dict)
        else:
            print(form.errors)
    return render(request, 'add_category.html', {'form': form})

from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            jiaoyubeijing = form.cleaned_data['jiaoyubeijing']
            gongzhuojingli = form.cleaned_data['gongzhuojingli']
            xiangmujingli = form.cleaned_data['xiangmujingli']
            jinengzhengshu = form.cleaned_data['jinengzhengshu']
            file = request.FILES.get('file')
            media_url = "media/static/images/"
            form = ContactForm()
            return render(request, 'login.html', {'name': name,'email': email,'phone': phone,'message': message,'jiaoyubeijing': jiaoyubeijing,
                                           'gongzhuojingli': gongzhuojingli,'xiangmujingli': xiangmujingli,'jinengzhengshu': jinengzhengshu,
                                                  'file':file,'media_url':media_url})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})



