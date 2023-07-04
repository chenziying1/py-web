# -*- coding: utf-8 -*-
# time:2023/6/9 10:56
# file froms.py
# outhor:czy
# email:1060324818@qq.com
from django import forms
from .models import message

class messageForm(forms.ModelForm):
    text = forms.CharField(max_length=128)
    date = forms.CharField(max_length=20)

    class Meta:
        model = message
        fields = ('text','date')

