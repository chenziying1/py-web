# -*- coding: utf-8 -*-
# time:2023/6/7 17:49
# file search.py
# outhor:czy
# email:1060324818@qq.com

"""
需求：
    根据命令行参数进行读取并返回数据
步骤：
    1.获取命令行参数
    2.读取文件 获取数据
    3.输出到指定文件

"""

# 1.获取命令行参数
import argparse

parser = argparse.ArgumentParser()
# 定义输出文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('-t', '--target')   #搜索词汇
args = parser.parse_args()
# 输出文件的路径
OUTPUT = args.output
target = args.target


# 2.读取文件,获取数据
def get_data():
    strs = ""
    with open("data.txt", "r", encoding="utf-8") as f:
        for i in f.readlines():
            if target in i:
                strs += i
    if strs != None:
        print("搜索成功!")
    f.close()
    return strs
# 3.输出到指定文件
def save_file(strs):
    global OUTPUT
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(strs)
    else:
        with open("output.txt", 'w') as f:
            f.write(strs)
    print("保存成功!")
    f.close()
    return

strs = get_data()
save_file(strs)

"""
在命令行调用中，不能使用这个
if __name__ == "__main__":
    strs = get_data()
    save_file(strs)
"""



