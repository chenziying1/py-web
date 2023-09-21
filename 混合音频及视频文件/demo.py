# -*- coding: utf-8 -*-
# time:2023/4/15 11:30
# file index.py
# outhor:czy
# email:1060324818@qq.com

import os
import subprocess

def video_add_mp4(file_name,mp4_file,i):
    outfile_name = "D:\\bili_sp\\" + f'new{i}.mp4'
    cmd = f'D:\\ruangjian\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe -i {mp4_file} -i {file_name} -acodec copy -vcodec copy {outfile_name}'
    print(cmd)
    subprocess.call(cmd,shell=True)


def rename_dir(work_dir):
    target = os.listdir(work_dir)
    if "audio.mp3" in target or "video.mp4" in target or "audio.MP3" in target or "video.MP4" in target:
        return
    for filename in target:
        # 获取得到文件后缀
        split_file = os.path.splitext(filename)
        if split_file[0] == "audio":
            newfile = split_file[0] + ".mp3"
            os.rename(  # 实现重命名操作
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile))
        if split_file[0] == "video":
            newfile = split_file[0] + ".mp4"
            os.rename(  # 实现重命名操作
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile))
    print(os.listdir(work_dir))  # 打印修改后文件信息
    return





filepath = "D:\\Download"
index = 0
for i in os.listdir(filepath):
    target = i
    filepath_two = "D:\\Download" + "\\" + str(target)
    target = os.listdir(filepath_two)
    filepath_next = filepath_two + "\\" + str(target[0])
    target = os.listdir(filepath_next)
    filepath_last = filepath_next + "\\" + str(target[0])
    rename_dir(filepath_last)

    a = filepath_last + "\\" + "video.mp4"  # 视频
    b = filepath_last + "\\" + "audio.mp3"  # 音频
    video_add_mp4(a, b,index)
    index += 1



