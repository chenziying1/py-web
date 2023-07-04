import requests
import re
import json
#https://www.bilibili.com/video/BV1jB4y1a7t3


def get_resqonse(url):
          headers = {
                    #记得修改referer
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
                    'Referer':'https://search.bilibili.com/all?keyword=%E4%BA%BA%E7%94%9F%E8%8B%A6%E7%9F%AD+%E7%AE%A1%E5%A5%BD%E4%BD%A0%E8%87%AA%E5%B7%B1&from_source=webtop_search&spm_id_from=333.1007'
                    }

          response = requests.get(url,headers = headers)
          return response

def response_parse(html):
          playinfo = re.findall("<script>window.__playinfo__=(.*?)</script>",html.text)[0]
          playinfo_json = json.loads(playinfo)
          #print(playinfo_json)
          title = re.findall("<title data-vue-meta=\"true\">(.*?)</title> ",html.text)[0]
          video_info = playinfo_json["data"]["dash"]["video"][0]["baseUrl"]
          audio_info = playinfo_json["data"]["dash"]["audio"][0]["baseUrl"]
          #print(video_info)
          #print(audio_info)
          #print(title)
          return [title,video_info,audio_info]

def save(datas):
          title = datas[0]
          video_data = get_resqonse(datas[1]).content
          audio_info = get_resqonse(datas[2]).content
          print(datas)
          
          while title.count('/') != 0:
                              title =  title.replace('/'," ")
                              print(title)
          
                    
          
          with open(title+'.mp4','wb') as f:
                    f.write(video_data)
          f.close()

          with open(title+'.mp3','wb') as f:
                    f.write(audio_info)
          f.close()

          print('爬取',datas[0],'完成')

url = input("请输入你想获取的视频的url地址：")
response = get_resqonse(url)
data = response_parse(response)
save(data)

          
