# -*- coding: utf-8 -*-
# time:2023/7/2 6:35
# file forms.py
# outhor:czy
# email:1060324818@qq.com
from django import forms
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

