import requests
import os
url = "http://img0.dili360.com/ga/M00/02/AB/wKgBzFQ26i2AWujSAA_-xvEYLbU441.jpg"
root = "D://pict//"
path = root + url.split('/')[-1]
try:
          if not os.path.exists(root):
                    os.mkdir(root)
          if not os.path.exists(path):
                    r = requests.get(url)
                    with open(path,'wb') as f:
                              f.write(r.content)
                              f.close()
                              print("文件保存成功")
          else:
                    print("文件已经存在")
except:
          print("爬取失败")
