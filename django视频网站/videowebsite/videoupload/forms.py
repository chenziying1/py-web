# -*- coding: utf-8 -*-
# time:2023/7/17 17:01
# file forms.py
# outhor:czy
# email:1060324818@qq.com

from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'video_file')

