# -*- coding: utf-8 -*-
# time:2023/2/19 23:01
# file index.py
# outhor:czy
# email:1060324818@qq.com

import requests
import re
import ffmpy3



html = requests.get("https://www.kanys.cc/filmplay/80990-1-1.html").text

url = re.findall("\"url\":\"(.*?)\",\"url_next\":",html)[0]
url = url.replace("\/","/")
url = url[:39] + "/hls"+url[39:]


ffmpy3.FFmpeg(executable='D:\\ruangjian\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe',inputs={url: None}, outputs={"name"+'.mp4':None}).run()





