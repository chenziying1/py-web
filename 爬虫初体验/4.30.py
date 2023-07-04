# -*- coding: utf-8 -*-
# time:2023/4/30 8:10
# file 4.30.py
# outhor:czy
# email:1060324818@qq.com

from urllib.request import urlopen, urlretrieve
import requests
from bs4 import BeautifulSoup

res = requests.get("https://dn-simplecloud.shiyanlou.com/courses/uid214893-20200325-1585103411810?imageView2/2/h/150/q/100")

with open("logo.jpg","wb") as f:
    f.write(res.content)

#urlretrieve("https://dn-simplecloud.shiyanlou.com/courses/uid214893-20200325-1585103411810?imageView2/2/h/150/q/100","logo.jpg")
#这样才是对的

#html = urlopen("https://dn-simplecloud.shiyanlou.com/courses/uid214893-20200325-1585103411810?imageView2/2/h/150/q/100")
#bsObj = BeautifulSoup(html,"lxml")
#imageLocation = bsObj.find("img")["src"]
#urlretrieve(imageLocation, "logo.jpg")
#如果是这样也会报错，因为返回的是字符串

#urlretrieve(html, "logo.jpg")
#TypeError: expected string or bytes-like object 直接下载会出现这样的错误
