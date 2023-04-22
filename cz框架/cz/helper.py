# -*- coding: utf-8 -*-
# time:2023/4/16 8:34
# file helper.py
# outhor:czy
# email:1060324818@qq.com

# 以“.”分割文件名，获取文件后缀类型
def parse_static_key(filename):
    return filename.split(".")[-1]