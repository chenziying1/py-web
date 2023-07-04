import requests
import json
import random
import os
import string
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'}
word = input("请输入关键字")
print(word)
dir_name = ''.join(random.sample(string.ascii_letters+string.digits,8))
print('当前图像将保存在',dir_name,'目录中')
os.mkdir(dir_name)
max_values = 100
current_value = 0
image_index = 1
while current_value < max_values:
          result = requests.get(
                               "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8166340658849966126&ipn=rj\
                                &ct=201326592&is=&fp=result&fr=&word={}\
                                &queryWord=%E5%A4%96%E6%98%9F%E4%BA%BA&cl=2&lm=-1&ie=utf-8\
                                &oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=\
                                &copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1\
                                &expermode=&nojc=&isAsync=&pn={}&rn=30&gsm=1e&1659677495055="
                                .format(word,current_value),headers = headers)
          json_str = result.content
          json_doc = str(json_str,'utf-8')
          #print(json_doc)
          imageresult = json.loads(json_doc)
          datas = imageresult['data']
          for record in datas:
                    url = record.get('middleURL')
                    if url != None:
                              print('正在下载图片：',url)
                              r = requests.get(url)
                              filename = dir_name + '/' + str(image_index).zfill(10)+".png"
                              with open(filename,'wb') as f:
                                        f.write(r.content)
                                        image_index += 1
          current_value += 30
print('图像下载完成')
