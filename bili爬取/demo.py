# -*- coding: utf-8 -*-
# time:2023/1/9 19:59
# file index.py
# outhor:czy
# email:1060324818@qq.com

import requests
import re
import json
import time
import ffmpeg

#1.获取数据
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Referer': 'https://www.bilibili.com/',
        'Origin': 'https://www.bilibili.com'
    }
    req = requests.get(url,headers=headers)
    if req.status_code == 200:
        return req
    else:
        print("获取失败!")

#2.分析数据
def get_source(data):
    playinfo = re.findall("<script>window.__playinfo__=(.*?)</script>", data.text)[0]
    playinfo_json = json.loads(playinfo)
    title = re.findall("<title data-vue-meta=\"true\">(.*?)</title> ", data.text)[0]
    video_info = playinfo_json["data"]["dash"]["video"][0]["baseUrl"]
    audio_info = playinfo_json["data"]["dash"]["audio"][0]["baseUrl"]
    return title, video_info, audio_info

#3.保存到指定文件夹
def save_file(title, video_info, audio_info):

    video_data = get_data(video_info).content
    audio_data = get_data(audio_info).content

    title = title.replace('/', " ")
    title = title.replace('~', " ")
    title = title.replace('|', " ")

    try:
        with open(title+".mp3","wb") as f:
            f.write(audio_data)
        f.close()
    except:
        print("写入程序失败!")
        return

    try:
        with open(title+".mp4","wb") as f:
            f.write(video_data)
        f.close()
    except:
        print("写入程序失败!")
        return

    print(title,"爬取成功!")

#4.合成
def hebing(title):
    title = title.replace('/', " ")
    title = title.replace('~', " ")
    title = title.replace('|', " ")

    video_path = title + '.mp4'
    audio_path = title + '.mp3'
    output_path = "./混合 " + title + '.mp4'

    process = (
        ffmpeg.output(
            ffmpeg.input(filename=video_path),
            ffmpeg.input(filename=audio_path),
            filename=output_path, vcodec='copy', acodec='aac', strict='experimental', pix_fmt='yuv720p')
    ).overwrite_output()

    ffmpeg_path = 'D:\\ruangjian\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'
    process.run_async(cmd=ffmpeg_path, pipe_stdin=True, pipe_stdout=False, pipe_stderr=False)
    time.sleep(1)
    print("混合完成！")


if __name__ == "__main__":
    url = input("请输入你想获取的视频的url地址:")
    data = get_data(url)
    title, video_info, audio_info = get_source(data)
    save_file(title, video_info, audio_info)
    hebing(title)




