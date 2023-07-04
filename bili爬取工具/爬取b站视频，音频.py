import requests
import re
import json
#https://https://www.bilibili.com/video/BV1bZ4y1a7QZ


def get_resqonse(url):
          headers = {
                    #记得修改referer
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
                    'Referer':'https://www.bilibili.com/',
                    'Origin':'https://www.bilibili.com',
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
          
          
          title =  title.replace('/'," ")
          title =  title.replace('~'," ")
          title =  title.replace('|'," ")
          print(title)

          try:
                    with open(title+'.mp4','wb') as f:
                              f.write(video_data)
                    f.close()
          except :
                    with open('2.mp4','wb') as f:
                              f.write(video_data)
                    f.close()

          try:
                    with open(title+'.mp3','wb') as f:
                              f.write(audio_info)
                    f.close()
          except :
                    with open('2.mp3','wb') as f:
                              f.write(audio_info)
                    f.close()
          


          print('爬取',datas[0],'完成')

url = input("请输入你想获取的视频的url地址：")
response = get_resqonse(url)
data = response_parse(response)
save(data)

          
