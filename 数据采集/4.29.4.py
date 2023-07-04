# -*- coding: utf-8 -*-
# time:2023/4/29 18:33
# file 4.29.4.py
# outhor:czy
# email:1060324818@qq.com
import socket
from urllib.request import urlopen

import socks

socks.set_default_proxy(socks.SOCKS5,"localhost", 9150)
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())

