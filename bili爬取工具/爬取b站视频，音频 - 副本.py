import requests
import re
import json
import ffmpeg
import time
#https://www.bilibili.com/video/BV1jB4y1a7t3

title_name = ""
headers = {
          #记得修改referer
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
          'Referer':'http://www.996dm.com/',
          #'Origin': 'https://www.bilibili.com',
          'Connection':'keep-alive'
          #http://www.996dm.com/play/1055-1-12.html

          }

def get_resqonse(url):
          #print(headers)
          response = requests.get(url,headers = headers)
          return response

def response_parse(html):
          playinfo = "缘之空"#re.findall("<script>window.__playinfo__=(.*?)</script>",html.text)[0]
          playinfo_json = "缘之空"#json.loads(playinfo)
          #print(playinfo_json)
          title = "缘之空"#re.findall("<title data-vue-meta=\"true\">(.*?)</title> ",html.text)[0]
          video_info = "缘之空"#playinfo_json["data"]["dash"]["video"][0]["baseUrl"]
          audio_info = "缘之空"#playinfo_json["data"]["dash"]["audio"][0]["baseUrl"]
          #print(video_info)
          #print(audio_info)
          #print(title)
          return [title,video_info,audio_info]

def save(datas):
          global title_name
          
          title = "yuanzhikong"
          video_data = get_resqonse("https://danmu.yhdmjx.com/m3u8.php?url=3SiU2LTmmodGggYXXJFCbMUwurdwPdO2EpFXPterifQhwOJrzhVtAvzqCRPG/FGi").content
          audio_info = get_resqonse("https://danmu.yhdmjx.com/m3u8.php?url=3SiU2LTmmodGggYXXJFCbMUwurdwPdO2EpFXPterifQhwOJrzhVtAvzqCRPG/FGi").content
          print(datas)
          
          
          title =  title.replace('/'," ")
          title =  title.replace('~'," ")
          title =  title.replace('|'," ")
          title_name = title
          print(title)
          print(title_name)

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

def hecheng():
          video_path = title_name+'.mp4'
          print(video_path)
          # 传入的音频路径
          audio_path = title_name+'.mp3'
          print(video_path)
          # 生成的视频名称，不要和上述的路径一致
          output_path = "C:\\Users\\HP\\Desktop\\音乐\\混合" + title_name+'.mp4'
 
          process = (
                      ffmpeg.output(
                          ffmpeg.input(filename=video_path),
                          ffmpeg.input(filename=audio_path),
                          filename=output_path, vcodec='copy', acodec='aac', strict='experimental', pix_fmt='yuv720p')
            ).overwrite_output()
 
          ffmpeg_path = 'D:\\ruangjian\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'
          process.run_async(cmd=ffmpeg_path, pipe_stdin=True, pipe_stdout=False, pipe_stderr=False)
 
          time.sleep(1)
          #process.communicate(str.encode("q"))
          #process.terminate()
          
url = input("请输入你想获取的视频的url地址：")
response = get_resqonse(url)
data = response_parse(response)
save(data)
hecheng()

          
