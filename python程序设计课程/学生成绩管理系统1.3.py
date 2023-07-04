# -*- coding: utf-8 -*-
# time:2022/10/19 11:18
# file 学生成绩管理系统1.3.py
# outhor:czy
# email:1060324818@qq.com

# -*- coding: utf-8 -*-
# time:2022/10/18 10:57
# file 学生成绩管理系统1.2.py
# outhor:czy
# email:1060324818@qq.com


'''
一个综合的学生成绩管理系统，要求能够管理若干个学生多门课程成绩，需要实现以下功能：
读取以数据文件形式存储的学生信息；
可以按学号增加、修改、删除学生的信息；
按照学号、姓名、名次等方式查询学生信息；
可以按照学号顺序浏览学生信息；
可以统计每门课的最高分、最低分和平均分；计算每个学生的总分并进行排名。

一共有四大功能版块 基本信息管理 学生成绩管理 考试成绩管理 根据条件查询

1.3版本更新 优化代码，修正错误的提示信息，新增了直方图显示学生成绩信息
'''

import csv
import os
from matplotlib import pyplot as plt

filename = "student_manager.csv"


#基本信息管理
class base:
    def __init__(self):
        pass

    def displayMenu(self):
        # 完成显示系统菜单的功能
        print("*" * 40)
        print("学 生 成 绩 管 理 系 统 ")
        print("1、基本信息管理")
        print("2、学生成绩管理")
        print("3、考试成绩管理")
        print("4、查询学生信息")
        print("5、返回学生信息管理系统")
        print("*" * 40)

    def displaybase(self):
        print("*" * 40)
        print("基 本 信 息 管 理")
        print("1、添加学生信息")
        print("2、删除学生信息")
        print("3、修改学生信息")
        print("4、按姓名查询学生信息")
        print("5、返回学生信息管理系统")
        print("*" * 40)


    # 完成添加学生信息的功能
    def addNewStu(self):

        name = input("请输入学生的姓名：")
        stuId = str(eval(input("请输入学生的学号：")))
        age = str(input("请输入学生的性别："))

        # 完成添加学生信息的功能
        chinese = eval(input("请输入学生的语文成绩："))
        math = eval(input("请输入学生的数学成绩："))
        english = eval(input("请输入学生的英语成绩："))

        # 将每个学生的信息添加到列表中
        gub = [(stuId,name,age,str(math),str(chinese),str(english),math+chinese+english)]
        with open(filename, 'a+', encoding='gbk',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(gub)
        print("成功录入学生信息!")

    # 完成删除学生信息的功能
    def delStu(self):

        delName = input("请输入你要删除的学生姓名：")
        flag = 0

        file_old = filename
        file_temp = 'test_temp.csv'

        with open(file_old, 'r', newline='', encoding='gbk') as f_old, \
                open(file_temp, 'w', newline='', encoding='gbk') as f_temp:
            f_csv_old = csv.reader(f_old)
            f_csv_temp = csv.writer(f_temp)
            for i, rows in enumerate(f_csv_old):  # 保留header
                if i == 0:
                    f_csv_temp.writerow(rows)
                    break
            for rows in f_csv_old:
                if rows[1] != delName:  # 删除第一列值为1的行
                    f_csv_temp.writerow(rows)
                else:
                    flag = 1
                    continue

        if flag == 1:
            print("删除成功!")
        else:
            print("查无此人!")

        os.remove(file_old)
        os.rename(file_temp, file_old)

    # 完成修改学生信息的功能
    def reviseStu(self):

        reviseName = input("请输入你要修改信息的学生姓名：")
        # 要修改学生的信息
        newStuId = input("请输入要修改后学生的学号：")
        newsex = input("请输入要修改后学生的性别：")

        file_old = filename
        flag = 0
        file_temp = 'test_temp.csv'

        with open(file_old, 'r', newline='', encoding='gbk') as f_old, \
                open(file_temp, 'w', newline='', encoding='gbk') as f_temp:
            f_csv_old = csv.reader(f_old)
            f_csv_temp = csv.writer(f_temp)
            for i, rows in enumerate(f_csv_old):  # 保留header
                if i == 0:
                    f_csv_temp.writerow(rows)
                    break
            for rows in f_csv_old:
                if rows[1] != reviseName:  # 删除第一列值为1的行
                    f_csv_temp.writerow(rows)
                else:
                    flag = 1
                    rows[0],rows[2] = newStuId,newsex
                    f_csv_temp.writerow(rows)

        if flag == 1:
            print("修改成功!")
        else:
            print("查无此人!")

        os.remove(file_old)
        os.rename(file_temp, file_old)

    # 完成查询学生信息的功能
    def inquireStu(self):
        inquireName = input("请输入你要查询的学生的姓名：")
        flag = 0

        with open(filename,'r',encoding="gbk",newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                if row[1] == inquireName:
                    print(row)
                    flag = 1

        if flag == 0:
            print("查无此人...")

# 学生成绩管理
class grades:
    def __init__(self):
        pass

    def displaybase(self):
        print("*" * 40)
        print("学 生 成 绩 管 理")
        print("1、删除学生成绩信息")
        print("2、修改学生成绩信息")
        print("3、按姓名查询学生成绩信息")
        print("4、按总分进行排名")
        print("5、返回学生信息管理系统")
        print("*" * 40)

    # 完成删除学生信息的功能
    def delStu(self):

        delName = input("请输入你要删除的学生姓名：")
        file_old = filename
        file_temp = 'test_temp.csv'

        with open(file_old, 'r', newline='', encoding='gbk') as f_old, \
                open(file_temp, 'w', newline='', encoding='gbk') as f_temp:
            f_csv_old = csv.reader(f_old)
            f_csv_temp = csv.writer(f_temp)
            for i, rows in enumerate(f_csv_old):  # 保留header
                if i == 0:
                    f_csv_temp.writerow(rows)
                    break
            for rows in f_csv_old:
                if rows[1] != delName:  # 删除第一列值为1的行
                    f_csv_temp.writerow(rows)
                else:
                    flag = 1
                    continue

        if flag == 1:
            print("删除成功!")
        else:
            print("查无此人!")

        os.remove(file_old)
        os.rename(file_temp, file_old)

    # 完成修改学生信息的功能
    def reviseStu(self):
        reviseName = input("请输入你要修改信息的学生姓名：")
        newchinese = input("请输入要修改后学生的语文成绩：")
        newmath = input("请输入要修改后学生的数学成绩：")
        newenglish = input("请输入要修改后学生的英语成绩：")
        file_old = filename
        flag = 0
        file_temp = 'test_temp.csv'

        with open(file_old, 'r', newline='', encoding='gbk') as f_old, \
                open(file_temp, 'w', newline='', encoding='gbk') as f_temp:
            f_csv_old = csv.reader(f_old)
            f_csv_temp = csv.writer(f_temp)
            for i, rows in enumerate(f_csv_old):  # 保留header
                if i == 0:
                    f_csv_temp.writerow(rows)
                    break
            for rows in f_csv_old:
                if rows[1] != reviseName:
                    f_csv_temp.writerow(rows)
                else:
                    flag = 1
                    rows[3], rows[4],rows[5],rows[6] = newmath, newchinese,newenglish,str(int(newmath)+int(newchinese)+int(newenglish))
                    f_csv_temp.writerow(rows)

        if flag == 1:
            print("修改成功!")
        else:
            print("查无此人!")

        os.remove(file_old)
        os.rename(file_temp, file_old)

    # 完成查询学生信息的功能
    def inquireStu(self):
        inquireName = input("请输入你要查询的学生的姓名：")
        flag = 0

        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                if row[1] == inquireName:
                    print(row)
                    flag = 1

        if flag == 0:
            print("查无此人...")

    #进行总分排名
    def sortgrades(self):
        stuList_grades = []

        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                stuList_grades.append([row[1],row[-1]])

        ans = sorted(stuList_grades, key=(lambda x: x[1]), reverse=True)
        print(ans)

# 考试成绩管理
class test_grades:
    def __init__(self):
        pass

    def displaybase(self):
        print("*" * 40)
        print("考 试 成 绩 管 理")
        print("1、查询课程最高分")
        print("2、查询课程最低分")
        print("3、查询课程平均分")
        print("4、按课程分数进行排名")
        print("5、直方图显示成绩信息")
        print("6、返回学生信息管理系统")
        print("*" * 40)

    #直方图显示课程成绩信息
    def hist_show(self):
        name = input("请输入课程名字：")
        if name == "chinese":
            number = 4
            name = "语文"
        elif name == "math":
            number = 3
            name = "数学"
        elif name == "english":
            number = 5
            name = "英语"

        gub = []
        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                if row[number] == "语文分数" or row[number] == "数学分数" or row[number] == "英语分数":
                    continue
                gub.append(int(row[number]))
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
        plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
        b = [40,50,60,70,80,90,100]
        plt.hist(gub, b, histtype='bar', facecolor='blue', edgecolor='black', alpha=0.7, rwidth=0.5)
        plt.grid(alpha=0.3)
        plt.legend()
        plt.xlabel(name+"成绩")
        plt.ylabel("不同分数段的人数")
        plt.title('matplotlib绘制直方图')
        plt.show()
        plt.show()

    # 完成查询课程最高分
    def frist_grades(self):

        name = input("请输入课程名字：")
        if name == "chinese":
            number = 4
        elif name == "math":
            number = 3
        elif name == "english":
            number = 5

        gub = []
        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                gub.append([row[1], row[number]])

        ans = sorted(gub, key=(lambda x: x[1]), reverse=True)[1]
        print(ans)

    # 完成查询课程最低分
    def last_grades(self):

        name = input("请输入课程名字：")
        if name == "chinese":
            number = 4
        elif name == "math":
            number = 3
        elif name == "english":
            number = 5

        gub = []
        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                gub.append([row[1], row[number]])

        ans = sorted(gub, key=(lambda x: x[1]), reverse=True)[-1]
        print(ans)

    # 完成查询课程平均分
    def average_score(self):
        name = input("请输入课程名字：")
        if name == "chinese":
            number = 4
        elif name == "math":
            number = 3
        elif name == "english":
            number = 5
        gub = []

        numbers = 0
        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                numbers += 1
                gub.append(int(row[number]))

        ans = sum(gub) // numbers
        print(ans)

    #课程排名
    def ranking(self):
        # 完成查询课程排名
        name = input("请输入课程名字：")
        if name == "chinese":
            number = 4
        elif name == "math":
            number = 3
        elif name == "english":
            number = 5
        else:
            print("请重新输入!")
        gub = []
        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                gub.append([row[1], row[number]])
        ans = sorted(gub, key=(lambda x: x[1]), reverse=True)
        print(ans)

    #总分排名
    def sortgrades(self):

        stuList_grades = []
        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                stuList_grades.append([row[1], row[-1]])
        f.close()
        ans = sorted(stuList_grades, key=(lambda x: x[1]), reverse=True)
        print(ans)

# 根据条件查询
class find:
    def __init__(self):
        pass

    def displaybase(self):
        print("*" * 40)
        print("根 据 条 件 查 询")
        print("1、按学号查询")
        print("2、按姓名查询")
        print("3、按名次查询")
        print("4、显示全部学生信息")
        print("5、返回学生信息管理系统")
        print("*" * 40)

    # 完成按学号查询
    def number(self):
        name = input("请输入学号：")
        flag = 0

        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                if row[0] == name:
                    print(row)
                    flag = 1

        if flag == 0:
            print("查无此人...")

    # 完成按姓名查询
    def name(self):
        name = input("请输入学生姓名：")
        flag = 0

        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                if row[1] == name:
                    print(row)
                    flag = 1

        if flag == 0:
            print("查无此人...")

    # 完成按名次查询
    def ranking(self):

        name = input("请输入查询的课程名称：")
        chi = eval(input("请输入查询的名次："))

        if name == "chinese":
            number = 4
        elif name == "math":
            number = 3
        elif name == "english":
            number = 5
        else:
            print("请重新输入!")
            return

        gub = []
        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                gub.append([row[1], row[number]])
        ans = sorted(gub, key=(lambda x: x[1]), reverse=True)

        truename = ans[chi][0]
        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                if row[1] == truename:
                    print(row)

    # 显示全部的学生
    def all(self):
        with open(filename, 'r', encoding="gbk", newline="") as f:
            rows = csv.reader(f)
            for row in rows:
                print(row)

# 主函数：程序从这里开始运行
def main():
    #判断文件是否存在
    if os.path.exists(filename):
        pass
    else:
        # 创建表
        headers = ['学号', '姓名', '性别', '数学分数', '语文分数', '英语分数', '总分']
        with open(filename, 'w', encoding='gbk', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

    # 菜单显示
    # 1、提示用户选择功能
    while True:
        # 2、获取用户的输入
        base.displayMenu("")
        key = int(input("请输入你选择的功能序号："))

        if key == 1:
                  while True:
                    base.displaybase('')
                    k = int(input("请输入你选择的功能序号："))
                    if k == 1:
                              base.addNewStu('')
                    elif k == 2:
                              base.delStu('')
                    elif k == 3:
                              base.reviseStu('')
                    elif k == 4:
                              base.inquireStu('')
                    elif k == 5:
                              print("已返回主菜单界面")
                              break
        elif key == 2:
            while True:
                grades.displaybase("")
                k = int(input("请输入你选择的功能序号："))
                if k == 1:
                    grades.delStu('')
                elif k == 2:
                    grades.reviseStu('')
                elif k == 3:
                    grades.inquireStu('')
                elif k == 4:
                    grades.sortgrades('')
                elif k == 5:
                    print("已返回主菜单界面")
                    break
        elif key == 3:
            while True:
                test_grades.displaybase('')
                k = int(input("请输入你选择的功能序号："))
                if k == 1:
                    test_grades.frist_grades('')
                elif k == 2:
                    test_grades.last_grades('')
                elif k == 3:
                    test_grades.average_score('')
                elif k == 4:
                    test_grades.ranking('')
                elif k == 5:
                    test_grades.hist_show('')
                elif k == 6:
                    print("已返回主菜单界面")
                    break
        elif key == 4:
            while True:
                find.displaybase('')
                k = int(input("请输入你选择的功能序号："))
                if k == 1:
                    find.number('')
                elif k == 2:
                    find.name('')
                elif k == 3:
                    find.ranking('')
                elif k == 4:
                    find.all('')
                elif k == 5:
                    print("已返回主菜单界面")
                    break
        elif key == 5:
            print('退出程序！！！')
            return
        else:
            print("输入有误，请重新输入！！！只能输入1-5的数字！！！")

        print("")

main()


