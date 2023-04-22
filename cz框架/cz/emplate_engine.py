# -*- coding: utf-8 -*-
# time:2023/4/16 8:34
# file emplate_engine.py
# outhor:czy
# email:1060324818@qq.com

import os
import re

pattern = r'{{(.*?)}}' #通过正则表达式判断那些需要置换

def parse_args(obj):

    comp = re.compile(pattern)  # 创建匹配对象
    result = comp.findall(obj)  # 获取匹配结果

    return result or () #如果有找到标记则返回，反之返回一个空的 tuple

def replace_template(app, path, **options): #在模板文件中查找并准备替换内容

    content = '<h1>Not Found Template.</h1>' #找不到时返回

    path = os.path.join(app.template_folder, path)#template_folder是模板文件的本地目录，在init里定义

    if os.path.exists(path):
        with open(path,'rb') as f:
            content = f.read().decode() #获取文件
        args = parse_args(content) #获取所有的标记
        if options:
            for arg in args:
                key = arg.strip() #从标记中获取键? 这是为什么？
                old_value = '{{{{{}}}}}'.format(arg)
                new_value = str(options.get(key, ''))
                content = content.replace(old_value, new_value)

    return content


