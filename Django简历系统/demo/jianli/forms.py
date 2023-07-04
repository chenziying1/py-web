# -*- coding: utf-8 -*-
# time:2023/7/2 6:35
# file forms.py
# outhor:czy
# email:1060324818@qq.com
from django import forms
from .models import xingxi

class xingxiForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    birthdate = forms.CharField(max_length=128, help_text="Please enter the category name.")
    classname = forms.CharField(max_length=128, help_text="Please enter the category name.")
    hoby = forms.CharField(max_length=128, help_text="Please enter the category name.")
    Personalstrengths = forms.CharField(max_length=128, help_text="Please enter the category name.")

    class Meta:
        model = xingxi
        fields = '__all__'

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message', 'jiaoyubeijing','gongzhuojingli', 'xiangmujingli', 'jinengzhengshu','file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'jiaoyubeijing': forms.Textarea(attrs={'class': 'form-control'}),
            'gongzhuojingli': forms.Textarea(attrs={'class': 'form-control'}),
            'xiangmujingli': forms.Textarea(attrs={'class': 'form-control'}),
            'jinengzhengshu': forms.Textarea(attrs={'class': 'form-control'}),
        }


from .models import Image
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'file')
