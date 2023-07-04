# -*- coding: utf-8 -*-
# time:2023/6/15 16:56
# file find_target.py
# outhor:czy
# email:1060324818@qq.com

import os
import openpyxl

class index():
    def __init__(self,indexs):
        self.indexs = indexs

    def res(self):
        path = r"D:\py-web\flask搜索引擎"
        os.chdir(path)  # 修改工作路径
        qizhi = False
        workbook = openpyxl.load_workbook('ans.xlsx')  # 返回一个workbook数据类型的值
        sheet = workbook.active  # 获取活动表
        ans = []
        for i in sheet.iter_rows(min_row=2, max_row=5, min_col=1, max_col=2):
            for j in i:
                if j.value == self.indexs:
                    qizhi = True
                if qizhi:
                    ans.append(j.value)
            if qizhi:
                break
        return ans

if __name__ == "__main__":
    create = index("百度")
    number = create.res()
    print(number)





