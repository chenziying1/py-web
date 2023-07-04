# -*- coding: utf-8 -*-
# time:2023/4/29 16:16
# file orc_test.py
# outhor:czy
# email:1060324818@qq.com

from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('D:\image.png'))
print(text)
