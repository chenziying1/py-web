# -*- coding: utf-8 -*-
# time:2023/7/26 9:27
# file index.py
# outhor:
# email:
# app.py

import base64
import hashlib
from datetime import datetime, timedelta
import mysql.connector
from cryptography.fernet import Fernet
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sa'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_yiyao'

个人邮箱 = "3337026057@qq.com"
个人授权码 = "ynqlpmbhrcspcjjf"

def get_mysql_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

@app.route('/search_drugs', methods=['POST'])
def search_drugs():
    drug_list = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]
    keyword = request.form.get('keyword')
    filtered_drugs = [drug for drug in drug_list if keyword.lower() in drug.lower()]
    return jsonify(filtered_drugs)

def encrypt_string(key, plaintext):
    f = Fernet(key)
    encrypted_data = f.encrypt(plaintext.encode('utf-8'))
    return encrypted_data

def decrypt_string(key, encrypted_data):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data

def hash_string(input_string):
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    return sha256.hexdigest()

@app.route('/new_page/<param1>/<param2>')
def new_page(param1, param2):
    return f"New Page with Parameters: param1={param1}, param2={param2}"



def 邮件提醒(patient_name,emails):

    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = 'SELECT 提醒时间 FROM 用药方案提醒 where 患者名称 = %s'
    cursor.execute(query, (patient_name,))
    second = cursor.fetchall()[0]
    connection.commit()
    cursor.close()

    current_time = datetime.now().time()
    given_time = datetime.strptime(second[0], "%H:%M:%S").time()

    if given_time > current_time:
        print("The given time is later than the current time.")
    else:
        import smtplib
        import email.utils
        from email.mime.text import MIMEText

        url = 'http://127.0.0.1:5007/hz_ywxx'

        # Email body with the URL
        email_body = f'''
        <p>Hello,</p>
        <p>请按时服药哦:</p>
        <p><a href="{url}">{url}</a></p>
        '''
        message = MIMEText(email_body, 'html')
        message['To'] = email.utils.formataddr((patient_name, emails))
        message['From'] = email.utils.formataddr(('flask医药管理系统', 个人邮箱))
        message['Subject'] = 'flask医药管理系统'
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(个人邮箱, 个人授权码)
        server.set_debuglevel(True)
        try:
            server.sendmail(个人邮箱, [emails], msg=message.as_string())
        finally:
            server.quit()

def 系统_患者药物提醒():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = 'SELECT * FROM 药物提醒 '
    cursor.execute(query, )
    second = cursor.fetchall()
    for i in second:
        患者名称 = i[1].encode('utf-8').decode('utf-8')
        提醒时间 = i[2]
        用药方案名称 = i[4]
        given_datetime = datetime.strptime(str(提醒时间), "%Y-%m-%d %H:%M:%S")
        current_datetime = datetime.now()
        if given_datetime > current_datetime:
            print("The given datetime is in the future.")
        else:
            query2 = 'SELECT * FROM hz where 用户名 = %s'
            cursor.execute(query2, (患者名称,))
            seconds = cursor.fetchall()
            print(seconds)
            邮件提醒(患者名称,seconds[0][-4])
            insert_query = "DELETE FROM 药物提醒 WHERE 患者名称 = %s and 用药方案名称 = %s"
            cursor.execute(insert_query, (患者名称,用药方案名称))

    connection.commit()
    cursor.close()


def 系统_患者用药方案提醒():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = 'SELECT * FROM 用药方案提醒 '
    cursor.execute(query,)
    second = cursor.fetchall()
    for i in second:
        患者名称 = i[1].encode('utf-8').decode('utf-8')
        提醒时间 = i[2]
        given_datetime = datetime.strptime(str(提醒时间), "%H:%M:%S")
        current_datetime = datetime.now()
        if given_datetime > current_datetime:
            print("The given datetime is in the future.")
        else:
            query2 = 'SELECT * FROM hz where 用户名 = %s'
            cursor.execute(query2, (患者名称,))
            seconds = cursor.fetchall()
            if seconds ==[]:
                pass
            else:
                邮件提醒(患者名称,seconds[0][-4])
                print("The given datetime is in the past or present.")
    connection.commit()
    cursor.close()


@app.route('/gly')
def gly():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    insert_query = "SELECT 用药名称 FROM 用药方案 "
    cursor.execute(insert_query,)
    users = cursor.fetchall()
    ans = {}
    for i in users:
        if i[0] not in ans:
            ans[i[0]] = 1
        else:
            ans[i[0]] += 1
    sorted_data = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    top_five = sorted_data[:5]
    connection.commit()
    cursor.close()
    data_points = []
    labels = []
    for i in top_five:
        data_points.append(i[1])
        labels.append(i[0])
    return render_template('gly_zy.html',data_points=data_points,labels=labels)

@app.route('/管理员_删除医生', methods=['POST'])
def 管理员_删除医生():
    data = request.get_json()
    account = data["account"]
    if account:
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "DELETE FROM ys WHERE 用户名 = %s"
        cursor.execute(insert_query, (account, ))
        insert_query2 = "DELETE FROM 管理用户 WHERE 医生名称 = %s"
        cursor.execute(insert_query2, (account,))
        connection.commit()
        cursor.close()
    return jsonify({"message": "Submission received successfully."})

@app.route('/管理员_删除药物', methods=['POST'])
def 管理员_删除药物():
    data = request.get_json()
    account = data["account"]
    if account:
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "DELETE FROM yw WHERE 药物名称 = %s"
        cursor.execute(insert_query, (account, ))
        connection.commit()
        cursor.close()
    return jsonify({"message": "Submission received successfully."})

@app.route('/管理员_删除患者', methods=['POST'])
def 管理员_删除患者():
    data = request.get_json()
    account = data["account"]
    if account:
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "DELETE FROM hz WHERE 用户名 = %s"
        cursor.execute(insert_query, (account, ))
        insert_query2 = "DELETE FROM 管理用户 WHERE 患者名称 = %s"
        cursor.execute(insert_query2, (account,))
        connection.commit()
        cursor.close()
    return jsonify({"message": "Submission received successfully."})

@app.route('/管理员_查看评价', methods=['GET','POST'])
def 管理员_查看评价():
    if request.method == "POST":
        用户名 = request.form.get('用户名')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "SELECT * FROM 评价 where 患者名称=%s"
        cursor.execute(insert_query,(用户名,))
        users = cursor.fetchall()
        if users == []:
            insert_query = "SELECT 患者名称 FROM 管理用户 where 医生名称=%s"
            cursor.execute(insert_query, (用户名,))
            second = cursor.fetchall()
            for i in second:

                #查看这个用户的全部评价的处方名称
                insert_query = "SELECT 处方名称 FROM 评价 where 患者名称=%s"
                cursor.execute(insert_query, (i[0],))
                four = cursor.fetchall()

                for j in four:
                    insert_query = "SELECT 医生名称 FROM  用药方案 where 处方名称=%s"
                    cursor.execute(insert_query, (j[0],))
                    five = cursor.fetchall()

                    if five[0][0] == 用户名:
                        #这里查数据
                        insert_query = "SELECT * FROM 评价 where 患者名称=%s and 处方名称=%s"
                        cursor.execute(insert_query, (i[0],j[0]))
                        three = cursor.fetchall()
                        users+=three
        connection.commit()
        cursor.close()
        return render_template('管理员_查看评价.html',users = users)
    return render_template('管理员_查看评价.html')

@app.route('/管理员_查看对应', methods=['GET','POST'])
def 管理员_查看对应():
    if request.method == "POST":
        用户名 = request.form.get('用户名')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "SELECT * FROM 管理用户 where 患者名称=%s or 医生名称=%s"
        cursor.execute(insert_query,(用户名,用户名,))
        users = cursor.fetchall()
        connection.commit()
        cursor.close()
        return render_template('管理员_查看对应.html',users = users)
    return render_template('管理员_查看对应.html')

@app.route('/管理员_转为患者', methods=['GET','POST'])
def 管理员_转为患者():
    if request.method == "POST":

        医生账号 = request.form.get('医生账号')

        connection = get_mysql_connection()
        cursor = connection.cursor()

        #获取名称--修改权限与状态--查询有没有这个患者--没有，加入
        insert_query = "UPDATE ys SET 状态='未启用' where 账号=%s "
        cursor.execute(insert_query, (医生账号,))

        insert_query2 = "SELECT * FROM ys where 账号=%s"
        cursor.execute(insert_query2,(医生账号,))
        users = cursor.fetchall()[0]

        insert_query3 = "SELECT * FROM hz where 账号=%s"
        cursor.execute(insert_query3, (医生账号,))
        users2 = cursor.fetchall()

        if users2 !=[]:
            insert_query = "UPDATE hz SET 状态='启用' where 账号=%s "
            cursor.execute(insert_query, (医生账号,))
        else:
            print(users)
            insert_query4 = "INSERT INTO hz (账号,用户名,密码,邮箱,健康档案权限,评价权限,用药管理权限,状态) VALUES (%s, %s,%s,%s,'是','是','是','启用')"
            cursor.execute(insert_query4, (医生账号, users[1], users[3],users[5]))


        insert_query5 = "SELECT 账号 FROM ys "
        cursor.execute(insert_query5, )
        users = cursor.fetchall()

        connection.commit()
        cursor.close()
        return render_template('管理员_转为患者.html',users = users)

    connection = get_mysql_connection()
    cursor = connection.cursor()
    insert_query = "SELECT 账号 FROM ys "
    cursor.execute(insert_query,)
    users = cursor.fetchall()
    connection.commit()
    cursor.close()
    return render_template('管理员_转为患者.html',users = users)

@app.route('/管理员_转为医生', methods=['GET','POST'])
def 管理员_转为医生():
    if request.method == "POST":

        患者账号 = request.form.get('患者账号')

        connection = get_mysql_connection()
        cursor = connection.cursor()

        #获取名称--修改权限与状态--查询有没有这个患者--没有，加入
        insert_query = "UPDATE hz SET 状态='未启用' where 账号=%s "
        cursor.execute(insert_query, (患者账号,))

        insert_query2 = "SELECT * FROM hz where 账号=%s"
        cursor.execute(insert_query2,(患者账号,))
        users = cursor.fetchall()[0]

        insert_query3 = "SELECT * FROM ys where 账号=%s"
        cursor.execute(insert_query3, (患者账号,))
        users2 = cursor.fetchall()

        if users2 !=[]:
            insert_query = "UPDATE ys SET 状态='启用' where 账号=%s "
            cursor.execute(insert_query, (患者账号,))
        else:
            print(users)
            insert_query4 = "INSERT INTO ys (账号,用户名,密码,邮箱,健康档案权限,评价权限,用药管理权限,状态,开处方权限,用药方案权限) VALUES (%s, %s,%s,%s,'是','是','是','启用')"
            cursor.execute(insert_query4, (患者账号, users[1], users[3],users[5]))


        insert_query5 = "SELECT 账号 FROM hz "
        cursor.execute(insert_query5, )
        users = cursor.fetchall()

        connection.commit()
        cursor.close()
        return render_template('管理员_转为医生.html',users = users)

    connection = get_mysql_connection()
    cursor = connection.cursor()
    insert_query = "SELECT 账号 FROM hz "
    cursor.execute(insert_query,)
    users = cursor.fetchall()
    connection.commit()
    cursor.close()
    return render_template('管理员_转为医生.html',users = users)

@app.route('/gly_ywglxg',methods=['GET', 'POST'])
def gly_ywglxg():
    if request.method == "POST":
        药物名称 = request.form.get('药物名称')
        药物厂商 = request.form.get('药物厂商')
        是否启用 = request.form.get('是否启用')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "UPDATE yw SET 药物厂商=%s,状态=%s WHERE 药物名称 = %s"
        cursor.execute(insert_query, (药物厂商, 是否启用,药物名称))
        connection.commit()
        cursor.close()
    return render_template('管理员_药物修改.html')

@app.route('/gly_ywglxz',methods=['GET', 'POST'])
def gly_ywglxz():
    if request.method == "POST":
        药物名称 = request.form.get('药物名称')
        药物厂商 = request.form.get('药物厂商')
        是否启用 = request.form.get('是否启用')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "INSERT INTO yw (药物名称,药物厂商,状态) VALUES (%s, %s,%s)"
        cursor.execute(insert_query, (药物名称, 药物厂商, 是否启用))
        connection.commit()
        cursor.close()
    return render_template('管理员_药物新增.html')

@app.route('/gly_hzqxxg',methods=['GET', 'POST'])
def gly_hzqxxg():
    if request.method == "POST":

        患者名称 = request.form.get('患者名称')
        健康档案 = request.form.get('健康档案')
        用药管理 = request.form.get('用药管理')
        评价 = request.form.get('评价')

        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "UPDATE hz SET 健康档案权限=%s,用药管理权限=%s,评价权限=%s WHERE 用户名 = %s"
        cursor.execute(insert_query, (健康档案, 用药管理, 评价, 患者名称))
        connection.commit()
        cursor.close()
    return render_template('管理员_患者权限修改.html')

@app.route('/gly_ysqxxg',methods=['GET', 'POST'])
def gly_ysqxxg():
    if request.method == "POST":
        医生名称 = request.form.get('医生名称')
        健康档案 = request.form.get('健康档案')
        用药管理 = request.form.get('用药管理')
        评价 = request.form.get('评价')
        是否开具处方 = request.form.get('是否开具处方')
        是否开具方案 = request.form.get('是否开具方案')

        connection = get_mysql_connection()
        cursor = connection.cursor()

        insert_query = "UPDATE ys SET 健康档案权限=%s,用药管理权限=%s,评价权限=%s,开处方权限=%s,用药方案权限=%s WHERE 用户名 = %s"
        cursor.execute(insert_query, (健康档案, 用药管理, 评价,是否开具处方,是否开具方案,医生名称))

        connection.commit()
        cursor.close()

    return render_template('管理员_医生权限修改.html')

@app.route('/gly_qxxz')
def gly_qxxz():
    return render_template('管理员_权限新增.html')

@app.route('/gly_glxg',methods=['GET', 'POST'])
def gly_glxg():
    if request.method == "POST":

        账号 = request.form.get('账号')
        用户名 = request.form.get('姓名')
        邮箱 = request.form.get('邮箱')
        状态 = request.form.get('状态')
        对应用户医生 = request.form.get('对应用户/医生') #用在其他表里面的

        connection = get_mysql_connection()
        cursor = connection.cursor()

        if 对应用户医生 == "无":
            insert_query = "UPDATE hz SET 用户名=%s, 邮箱=%s, 状态=%s  WHERE 账号 = %s"
            cursor.execute(insert_query, (用户名, 邮箱, 状态, 账号))
        else:
            insert_query3 = "SELECT 用户名 FROM hz where 账号 = %s "
            cursor.execute(insert_query3, (账号,))
            xinming = cursor.fetchall()[0][0]

            insert_query = "UPDATE hz SET 用户名=%s, 邮箱=%s, 状态=%s  WHERE 账号 = %s"
            cursor.execute(insert_query, (用户名, 邮箱, 状态, 账号))

            # 强制修改只要存在就修改
            insert_query4 = "UPDATE 管理用户 SET 患者名称=%s WHERE 患者名称=%s"
            cursor.execute(insert_query4, (用户名, xinming))

            insert_query2 = "SELECT * FROM 管理用户 where 医生名称=%s and 患者名称=%s "
            cursor.execute(insert_query2, (对应用户医生, 用户名))
            frist = cursor.fetchall()

            if frist != []:
                pass
            else:
                insert_query3 = "INSERT INTO 管理用户 (医生名称,患者名称) VALUES (%s, %s)"
                cursor.execute(insert_query3, (对应用户医生, 用户名))

        connection.commit()
        cursor.close()

    connection = get_mysql_connection()
    cursor = connection.cursor()

    insert_query = "SELECT 用户名 FROM ys where 状态='启用' "
    cursor.execute(insert_query, )
    frist = cursor.fetchall()

    connection.commit()
    cursor.close()

    return render_template('管理员_管理修改.html',users = frist)


@app.route('/gly_glxg2', methods=['GET', 'POST'])
def gly_glxg2():
    if request.method == "POST":
        账号 = request.form.get('账号')
        用户名 = request.form.get('姓名')
        邮箱 = request.form.get('邮箱')
        类型 = request.form.get('类型')
        状态 = request.form.get('状态')
        对应用户医生 = request.form.get('对应用户/医生')  # 用在其他表里面的

        connection = get_mysql_connection()
        cursor = connection.cursor()

        insert_query3 = "SELECT 用户名 FROM ys where 账号 = %s "
        cursor.execute(insert_query3, (账号,))
        xinming = cursor.fetchall()[0][0]

        insert_query = "UPDATE ys SET 用户名=%s, 邮箱=%s, 状态=%s  WHERE 账号 = %s"
        cursor.execute(insert_query, (用户名, 邮箱, 状态, 账号))

        # 强制修改只要存在就修改
        insert_query4 = "UPDATE 管理用户 SET 医生名称=%s WHERE 医生名称=%s"
        cursor.execute(insert_query4, (用户名, xinming))

        #先查找，后修改
        insert_query2 = "SELECT * FROM 管理用户 where 医生名称 = %s and 患者名称 = %s "
        cursor.execute(insert_query2, (用户名, 对应用户医生))
        frist = cursor.fetchall()

        if frist != []:
            pass
        else:
            insert_query3 = "INSERT INTO 管理用户 (医生名称,患者名称) VALUES (%s, %s)"
            cursor.execute(insert_query3, (对应用户医生, 用户名))

        connection.commit()
        cursor.close()

    connection = get_mysql_connection()
    cursor = connection.cursor()

    insert_query = "SELECT 用户名 FROM hz where 状态='启用' "
    cursor.execute(insert_query, )
    frist = cursor.fetchall()

    connection.commit()
    cursor.close()

    return render_template('管理员_管理修改2.html', users=frist)


@app.route('/gly_glxz',methods=['GET', 'POST'])
def gly_glxz():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    insert_query = "SELECT * FROM ys where 状态='启用' "
    cursor.execute(insert_query, )
    users = cursor.fetchall()
    connection.commit()
    cursor.close()

    if request.method == "POST":

        账号 = request.form.get('账号')
        用户名 = request.form.get('姓名')
        邮箱 = request.form.get('邮箱')
        类型 = request.form.get('类型')
        状态 = request.form.get('状态')
        对应用户医生 = request.form.get('对应医生') #用在其他表里面的
        密码 = "123456"
        encrypted_data = generate_password_hash(密码)

        if 类型 == "患者":

            connection = get_mysql_connection()
            cursor = connection.cursor()

            insert_query2 = "SELECT * FROM hz where 账号 = %s "
            cursor.execute(insert_query2, (账号,))
            users1 = cursor.fetchall()

            insert_query3 = "SELECT * FROM ys where 账号 = %s "
            cursor.execute(insert_query3, (账号,))
            users2 = cursor.fetchall()

            if users1 != [] or users2 != []:
                tishi = "当前账户已存在！"
                return render_template('管理员_管理新增.html',users=users,tishi=tishi)

            insert_query = "INSERT INTO hz (账号, 用户名, 邮箱, 状态, 密码,健康档案权限,用药管理权限,评价权限) VALUES (%s, %s,%s, %s,%s,'是','是','是')"
            cursor.execute(insert_query, (账号, 用户名, 邮箱, 状态, encrypted_data))

            insert_query2 = "SELECT * FROM 管理用户 where 医生名称= %s and 患者名称 = %s "
            cursor.execute(insert_query2, (对应用户医生,用户名))
            users = cursor.fetchall()
            if users != []:
                connection.commit()
                cursor.close()
                return render_template('管理员_管理新增.html',users=users)
            elif 对应用户医生 == "无":
                connection.commit()
                cursor.close()
                return render_template('管理员_管理新增.html',users=users)
            else:
                insert_query3 = "INSERT INTO 管理用户 (医生名称,患者名称) VALUES (%s, %s)"
                cursor.execute(insert_query3, (对应用户医生,用户名))

            connection.commit()
            cursor.close()
        else:
            print("什么也不是！")

    return render_template('管理员_管理新增.html',users=users)

@app.route('/gly_glxz2',methods=['GET', 'POST'])
def gly_glxz2():

    connection = get_mysql_connection()
    cursor = connection.cursor()
    insert_query = "SELECT * FROM hz where 状态='启用' "
    cursor.execute(insert_query, )
    users = cursor.fetchall()
    connection.commit()
    cursor.close()

    if request.method == "POST":

        账号 = request.form.get('账号')
        用户名 = request.form.get('姓名')
        邮箱 = request.form.get('邮箱')
        类型 = request.form.get('类型')
        状态 = request.form.get('状态')
        对应用户医生 = request.form.get('对应用户') #用在其他表里面的
        密码 = "123456"
        encrypted_data = generate_password_hash(密码)

        if 类型 == "医生":
            connection = get_mysql_connection()
            cursor = connection.cursor()

            insert_query2 = "SELECT * FROM hz where 账号 = %s "
            cursor.execute(insert_query2, (账号,))
            users1 = cursor.fetchall()

            insert_query3 = "SELECT * FROM ys where 账号 = %s "
            cursor.execute(insert_query3, (账号,))
            users2 = cursor.fetchall()

            if users1 != [] or users2 != []:
                tishi = "当前账户已存在！"
                connection.commit()
                cursor.close()
                return render_template('管理员_管理新增2.html', users=users, tishi=tishi)

            insert_query = "INSERT INTO ys (账号, 用户名, 邮箱, 状态, 密码,开处方权限,用药方案权限,健康档案权限,用药管理权限,评价权限) VALUES (%s, %s,%s, %s,%s,'是','是','否','否','否')"
            cursor.execute(insert_query, (账号, 用户名, 邮箱, 状态, encrypted_data))

            if 对应用户医生 == "无":
                tishi = "您已成功新增用户!"
                connection.commit()
                cursor.close()
                return render_template('管理员_管理新增2.html', users=users,tishi=tishi)

            insert_query2 = "SELECT * FROM 管理用户 where 医生名称= %s and 患者名称 = %s "
            cursor.execute(insert_query2, (对应用户医生, 用户名))
            users = cursor.fetchall()

            if users != []:
                pass
            else:
                insert_query3 = "INSERT INTO 管理用户 (医生名称,患者名称) VALUES (%s, %s)"
                cursor.execute(insert_query3, (用户名,对应用户医生))

            connection.commit()
            cursor.close()
        else:
            print("什么也不是！")

    return render_template('管理员_管理新增2.html',users=users)

@app.route('/gly_hzgl',methods=['GET', 'POST'])
def gly_hzgl():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM hz')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    if request.method == "POST":
        input_text = request.form.get('input_text')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "SELECT * FROM hz WHERE 用户名 = %s"
        cursor.execute(insert_query, (input_text,))
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('gly_hzgl.html', users=users)
    return render_template('gly_hzgl.html',users=users)

@app.route('/gly_hzgx',methods=['GET', 'POST'])
def gly_hzgx():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT 用户名,健康档案权限,用药管理权限,评价权限 FROM hz')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    if request.method == "POST":
        input_text = request.form.get('input_text')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "SELECT 用户名,健康档案权限,用药管理权限,评价权限 FROM hz WHERE 用户名 = %s"
        cursor.execute(insert_query, (input_text,))
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('gly_hzqx.html', users=users)
    return render_template('gly_hzqx.html',users=users)

@app.route('/gly_ysgl',methods=['GET', 'POST'])
def gly_ysgl():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ys')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    if request.method == "POST":
        input_text = request.form.get('input_text')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "SELECT * FROM ys WHERE 用户名 = %s"
        cursor.execute(insert_query, (input_text,))
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('gly_ysgl.html', users=users)
    return render_template('gly_ysgl.html',users=users)

@app.route('/gly_ysqx',methods=['GET', 'POST'])
def gly_ysqx():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT 用户名,开处方权限,用药方案权限,健康档案权限,用药管理权限,评价权限 FROM ys')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    if request.method == "POST":
        input_text = request.form.get('input_text')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "SELECT 用户名,开处方权限,用药方案权限,健康档案权限,用药管理权限,评价权限 FROM ys WHERE 用户名 = %s"
        cursor.execute(insert_query, (input_text,))
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('gly_ysqx.html', users=users)
    return render_template('gly_ysqx.html',users=users)

@app.route('/gly_ywgl',methods=['GET', 'POST'])
def gly_ywgl():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM yw')
    users = cursor.fetchall()
    cursor.close()
    connection.close()

    if request.method == "POST":
        input_text = request.form.get('input_text')
        if "or" in input_text:
            input_list = input_text.split(" ")
            connection = get_mysql_connection()
            cursor = connection.cursor()
            insert_query = "SELECT * FROM yw WHERE 状态 = %s or 药物名称 = %s"
            cursor.execute(insert_query, (input_list[2],input_list[0]))
            users = cursor.fetchall()
            cursor.close()
            connection.close()
        elif "and" in input_text:
            input_list = input_text.split(" ")
            connection = get_mysql_connection()
            cursor = connection.cursor()
            insert_query = "SELECT * FROM yw WHERE 状态 = %s and 药物名称 = %s"
            cursor.execute(insert_query, (input_list[2],input_list[0]))
            users = cursor.fetchall()
            cursor.close()
            connection.close()
        else:
            connection = get_mysql_connection()
            cursor = connection.cursor()
            insert_query = "SELECT * FROM yw WHERE 状态 = %s"
            cursor.execute(insert_query, (input_text,))
            users = cursor.fetchall()
            cursor.close()
            connection.close()
        return render_template('gly_ywgl.html', users=users)

    return render_template('gly_ywgl.html',users = users)

@app.route('/ys')
def ys():
    doctor_name = request.cookies.get('doctor_name')
    connection = get_mysql_connection()
    cursor = connection.cursor()

    query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (doctor_name, doctor_name))
    name = cursor.fetchall()[0][0]

    insert_query = "SELECT 用药名称,患者名称,实际服用时间,计划服用时间 FROM 用药方案 where 医生名称 = %s"
    cursor.execute(insert_query,(name,))
    users = cursor.fetchall()
    ans = {}
    zhunshi = []
    buzhunshi = []
    for i in users:
        if i[0] not in ans:
            ans[i[0]] = 1
        else:
            ans[i[0]] += 1

        if i[2] == "无":
            continue
        else:
            given_datetime = datetime.strptime(i[2], "%Y-%m-%d %H:%M:%S")
            current_datetime = datetime.strptime(i[3], "%Y-%m-%d %H:%M:%S")
            time_difference = current_datetime - given_datetime
            one_hour = timedelta(hours=1)
            if time_difference >= one_hour:
                zhunshi.append(i[1])
            else:
                buzhunshi.append(i[1])
    sorted_data = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    top_five = sorted_data[:5]
    #print(top_five)
    connection.commit()
    cursor.close()
    data_points = []
    labels = []
    for i in top_five:
        data_points.append(i[1])
        labels.append(i[0])
    zhunshi = list(set(zhunshi))
    buzhunshi = list(set(buzhunshi))
    return render_template('ys_zy.html', data_points=data_points, labels=labels,zhunshi=zhunshi,buzhunshi=buzhunshi,zhunshiren=len(zhunshi),buzhunshiren=len(buzhunshi),)

@app.route('/医生_删除方案', methods=['POST'])
def 医生_删除方案():
    data = request.get_json()
    name1 = data["name1"]
    name2 = data["name2"]
    connection = get_mysql_connection()
    cursor = connection.cursor()
    insert_query = "DELETE FROM 用药方案 WHERE 处方名称= %s and 患者名称= %s"
    cursor.execute(insert_query, (name1, name2))
    connection.commit()
    cursor.close()
    return jsonify({"message": "Submission received successfully."})

@app.route('/医生_删除患者', methods=['POST'])
def 医生_删除患者():
    data = request.get_json()
    account = data['account']

    doctor_name = request.cookies.get('doctor_name')

    connection = get_mysql_connection()
    cursor = connection.cursor()

    query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (doctor_name, doctor_name))
    name = cursor.fetchall()[0][0]

    insert_query = "DELETE FROM 管理用户 WHERE 医生名称 = %s and 患者名称= %s"
    cursor.execute(insert_query, (name, account))

    connection.commit()
    cursor.close()

    return jsonify({"message": "Submission received successfully."})

@app.route('/管理员_重置密码', methods=['GET','POST'])
def 管理员_重置密码():
    if request.method == "POST":
        用户名 = request.form.get('用户名')
        类型 = request.form.get('类型')
        密码 = '123456'
        encrypted_data = generate_password_hash(密码)

        connection = get_mysql_connection()
        cursor = connection.cursor()


        if 类型 == "医生":
            insert_query = "UPDATE ys SET 密码=%s WHERE 用户名 = %s"
            cursor.execute(insert_query, (encrypted_data,用户名,))
        elif 类型 == "患者":
            insert_query = "UPDATE hz SET 密码=%s WHERE 用户名 = %s"
            cursor.execute(insert_query, (encrypted_data,用户名,))

        connection.commit()
        cursor.close()

    return render_template('管理员_重置密码.html')


@app.route('/ys_kcfxz', methods=['GET','POST'])
def ys_kcfxz():
    doctor_name = request.cookies.get('doctor_name')

    connection = get_mysql_connection()
    cursor = connection.cursor()

    query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (doctor_name, doctor_name))
    name = cursor.fetchall()[0][0]

    querys3 = 'SELECT 药物名称 FROM yw where 状态 = %s '
    cursor.execute(querys3, ('启用',))
    frist = cursor.fetchall()

    querys = 'SELECT 患者名称 FROM 管理用户 where 医生名称=%s '
    cursor.execute(querys, (name,))
    second = cursor.fetchall()

    if request.method == "POST":

        处方名称 = request.form.get('处方名称')
        患者名称 = request.form.get('患者名称')
        用药名称 = request.form.get('用药名称')
        用药计量 = request.form.get('用药计量')
        时间 = datetime.now()

        #首先，形成时间，最后插入数据库中
        timestamp = datetime.strptime(str(时间), "%Y-%m-%d %H:%M:%S.%f")
        new_timestamp = timestamp + timedelta(days=1)
        new_timestamp = new_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
        new_timestamp_string = str(new_timestamp).split(" ")[0]

        # 检查是否早就存在
        query4 = 'SELECT 处方名称 FROM 用药方案 where 医生名称 = %s and 处方名称 = %s'
        cursor.execute(query4, (name, 处方名称))
        frist2 = cursor.fetchall()
        if frist2 != [] :
            return render_template('医生_开具处方.html', drug=frist, second=second)

        if 用药计量 == "一天一次":
            time = new_timestamp_string + " 07:00:00"
            insert_query = "INSERT INTO 用药方案 (处方名称, 患者名称, 用药名称, 用药计量, 时间,状态,备注,医生名称,实际服用时间,计划服用时间) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'无',%s)"
            cursor.execute(insert_query, (处方名称, 患者名称, 用药名称, 用药计量, 时间, "未启用", "无", name, time))

            connection.commit()
            cursor.close()

        elif 用药计量 == "一天两次":
            time = new_timestamp_string + " 07:00:00"
            insert_query = "INSERT INTO 用药方案 (处方名称, 患者名称, 用药名称, 用药计量, 时间,状态,备注,医生名称,实际服用时间,计划服用时间) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'无',%s)"
            cursor.execute(insert_query, (处方名称, 患者名称, 用药名称, 用药计量, 时间, "未启用", "无", name, time))

            time2 = new_timestamp_string + " 12:00:00"
            insert_query2 = "INSERT INTO 用药方案 (处方名称, 患者名称, 用药名称, 用药计量, 时间,状态,备注,医生名称,实际服用时间,计划服用时间) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'无',%s)"
            cursor.execute(insert_query2, (处方名称, 患者名称, 用药名称, 用药计量, 时间, "未启用", "无", name, time2))

            connection.commit()
            cursor.close()

        else:
            time = new_timestamp_string + " 07:00:00"
            insert_query = "INSERT INTO 用药方案 (处方名称, 患者名称, 用药名称, 用药计量, 时间,状态,备注,医生名称,实际服用时间,计划服用时间) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'无',%s)"
            cursor.execute(insert_query, (处方名称, 患者名称, 用药名称, 用药计量, 时间, "未启用", "无", name, time))

            time2 = new_timestamp_string + " 12:00:00"
            insert_query2 = "INSERT INTO 用药方案 (处方名称, 患者名称, 用药名称, 用药计量, 时间,状态,备注,医生名称,实际服用时间,计划服用时间) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'无',%s)"
            cursor.execute(insert_query2, (处方名称, 患者名称, 用药名称, 用药计量, 时间, "未启用", "无", name, time2))

            time3 = new_timestamp_string + " 18:00:00"
            insert_query3 = "INSERT INTO 用药方案 (处方名称, 患者名称, 用药名称, 用药计量, 时间,状态,备注,医生名称,实际服用时间,计划服用时间) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'无',%s)"
            cursor.execute(insert_query3, (处方名称, 患者名称, 用药名称, 用药计量, 时间, "未启用", "无", name, time3))

            connection.commit()
            cursor.close()

    connection.commit()
    cursor.close()

    return render_template('医生_开具处方.html',drug=frist,second=second)


@app.route('/ys_kcf')
def ys_kcf():
    doctor_name = request.cookies.get('doctor_name')
    connection = get_mysql_connection()
    cursor = connection.cursor()

    query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (doctor_name, doctor_name))
    doctor_name = cursor.fetchall()[0][0]

    query3 = 'SELECT 开处方权限 FROM ys where 用户名 = %s or 账号 = %s'
    cursor.execute(query3, (doctor_name, doctor_name))
    开处方权限 = cursor.fetchall()[0][0]

    if 开处方权限 == "否":
        return render_template("无权访问.html")

    querys = 'SELECT 患者名称 FROM 管理用户 where 医生名称 = %s'
    cursor.execute(querys, (doctor_name,))
    frist = cursor.fetchall()
    connection.commit()
    cursor.close()
    return render_template('ys_kcf.html',users = frist)

@app.route('/ys_yyfa', methods=['GET','POST'])
def ys_yyfa():
    doctor_name = request.cookies.get('doctor_name')
    if request.method == "POST":
        data = request.form.get("input_text")
        connection = get_mysql_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM 用药方案')
        users = cursor.fetchall()
        ans = []
        for i in users:
            if data in i[1]:
                ans.append(i)
        cursor.close()
        connection.close()
        return render_template('ys_yyfa.html', users=ans)
    connection = get_mysql_connection()
    cursor = connection.cursor()

    query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (doctor_name, doctor_name))
    doctor_name = cursor.fetchall()[0][0]

    query3 = 'SELECT 用药方案权限 FROM ys where 用户名 = %s or 账号 = %s'
    cursor.execute(query3, (doctor_name, doctor_name))
    用药方案权限 = cursor.fetchall()[0][0]

    if 用药方案权限 == "否":
        return render_template("无权访问.html")


    cursor.execute('SELECT * FROM 用药方案 where 医生名称=%s',(doctor_name,))
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('ys_yyfa.html',users=users)

def 发送用药方案邮件(users,user):
    import smtplib
    import email.utils
    from email.mime.text import MIMEText
    url = 'http://127.0.0.1:5007/hz_ywxx'

    # Email body with the URL
    email_body = f'''
                        <p>Hello,</p>
                        <p>请按时服药哦:</p>
                        <p><a href="{url}">{url}</a></p>
                        '''
    message = MIMEText(email_body, 'html')
    message['To'] = email.utils.formataddr((users[0][0], user[0][0]))
    message['From'] = email.utils.formataddr(('flask医药管理系统', 个人邮箱))
    message['Subject'] = 'flask医药管理系统'
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login(个人邮箱, 个人授权码)
    server.set_debuglevel(True)
    try:
        server.sendmail(个人邮箱, [user[0][0]], msg=message.as_string())
    finally:
        server.quit()

@app.route('/ys_yyfaxg',methods=['GET', 'POST'])
def ys_yyfaxg():
    doctor_name = request.cookies.get('doctor_name')
    if request.method == "POST":
        处方名称 = request.form.get('处方名称')
        备注 = request.form.get('备注')
        状态 = request.form.get('状态')
        connection = get_mysql_connection()
        cursor = connection.cursor()

        query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
        cursor.execute(query2, (doctor_name, doctor_name))
        doctor_name = cursor.fetchall()[0][0]

        insert_query = "UPDATE 用药方案 SET 备注=%s, 状态=%s WHERE 处方名称 = %s"
        cursor.execute(insert_query, ( 备注, 状态, 处方名称))

        querys = 'SELECT 患者名称 FROM 用药方案 where 医生名称 = %s and 处方名称 = %s'
        cursor.execute(querys, (doctor_name,处方名称))
        users = cursor.fetchall()
        if users != []:
            querys2 = 'SELECT 邮箱 FROM hz where 用户名 = %s'
            cursor.execute(querys2, (users[0][0],))
            user = cursor.fetchall()

            发送用药方案邮件(users,user)

        connection.commit()
        cursor.close()

    connection = get_mysql_connection()
    cursor = connection.cursor()

    query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (doctor_name, doctor_name))
    doctor_name = cursor.fetchall()[0][0]

    querys = 'SELECT 处方名称 FROM 用药方案 where 医生名称 = %s '
    cursor.execute(querys, (doctor_name,))
    frist = cursor.fetchall()
    ans = []
    for i in frist:
        ans.append(i[0])
    ans = list(set(ans))

    connection.commit()
    cursor.close()

    return render_template('医生_修改方案.html',frist=ans)

@app.route('/ys_yyfaxg2',methods=['GET', 'POST'])
def ys_yyfaxg2():
    if request.method == "POST":
        处方名称 = request.form.get('处方名称')
        患者名称 = request.form.get('患者名称')
        用药名称 = request.form.get('用药名称')
        用药计量 = request.form.get('用药计量')
        备注 = request.form.get('备注')
        状态 = request.form.get('状态')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        insert_query = "UPDATE 用药方案 SET 患者名称=%s, 用药名称=%s, 用药计量=%s, 备注=%s, 状态=%s WHERE 处方名称 = %s"
        cursor.execute(insert_query, (患者名称, 用药名称, 用药计量, 备注, 状态, 处方名称))
        connection.commit()
        cursor.close()

    connection = get_mysql_connection()
    cursor = connection.cursor()

    query2 = 'SELECT 药物名称 FROM yw where 状态 = "启用" '
    cursor.execute(query2, )
    药物名称 = cursor.fetchall()

    connection.commit()
    cursor.close()

    return render_template('医生_修改方案2.html',药物名称=药物名称)

@app.route('/ys_yhglxz',methods=['GET', 'POST'])
def ys_yhglxz():
    if request.method == "POST":
        doctor_name = request.cookies.get('doctor_name')

        姓名 = request.form.get('姓名')

        connection = get_mysql_connection()
        cursor = connection.cursor()

        query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
        cursor.execute(query2, (doctor_name, doctor_name))
        doctor_name = cursor.fetchall()[0][0]


        insert_query = "INSERT INTO 管理用户 (医生名称, 患者名称) VALUES (%s,%s)"
        cursor.execute(insert_query, (doctor_name,姓名))
        connection.commit()
        cursor.close()

    connection = get_mysql_connection()
    cursor = connection.cursor()
    querys = 'SELECT * FROM hz where 状态 = "启用" '
    cursor.execute(querys, )
    frist = cursor.fetchall()
    connection.commit()
    cursor.close()

    return render_template('医生_新增患者.html',users = frist)

@app.route('/ys_yhglxg',methods=['GET', 'POST'])
def ys_yhglxg():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
    return render_template('医生_修改患者.html')

@app.route('/ys_yhgl',methods=['GET', 'POST'])
def ys_yhgl():
    doctor_name = request.cookies.get('doctor_name')
    connection = get_mysql_connection()
    cursor = connection.cursor()

    query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (doctor_name, doctor_name))
    doctor_name = cursor.fetchall()[0][0]

    querys = 'SELECT 患者名称 FROM 管理用户 where 医生名称 = %s'
    cursor.execute(querys,(doctor_name,))
    frist = cursor.fetchall()
    users = []
    for i in frist:
        query = 'SELECT * FROM hz where 用户名 = %s'
        cursor.execute(query, (i[0],))
        second = cursor.fetchall()
        users += second

    cursor.close()
    connection.close()

    if request.method == "POST":
        input_text = request.form.get('input_text')
        connection = get_mysql_connection()
        cursor = connection.cursor()
        querys = 'SELECT 患者名称 FROM 管理用户 where 医生名称 = %s and 患者名称 = %s'
        cursor.execute(querys, (doctor_name, input_text))
        second = cursor.fetchall()
        frist = []
        for i in second:
            if input_text in i[0] :
                frist.append(i)
        users = []
        for i in frist:
            query = 'SELECT * FROM hz where 用户名 = %s'
            cursor.execute(query, (i[0],))
            second = cursor.fetchall()
            users += second
        cursor.close()
        connection.close()

        return render_template('ys_yhgl.html', users=users)


    return render_template('ys_yhgl.html',users=users)

@app.route('/ys_xgmm',methods=['GET', 'POST'])
def ys_xgmm():
    if request.method == "POST":
        doctor_name = request.cookies.get('doctor_name')

        密码 = request.form.get('密码')
        确认密码 = request.form.get('确认密码')
        if 密码 != 确认密码:
            tishi = "两次密码不一样!"
            return render_template('医生_修改密码.html',tishi = tishi)

        encrypted_data = generate_password_hash(密码)

        connection = get_mysql_connection()
        cursor = connection.cursor()

        query2 = 'SELECT 用户名 FROM ys where 用户名 = %s or 账号 = %s'
        cursor.execute(query2, (doctor_name, doctor_name))
        doctor_name = cursor.fetchall()[0][0]

        insert_query = "UPDATE ys SET 密码=%s WHERE 用户名 = %s"
        cursor.execute(insert_query, (encrypted_data,doctor_name))

        connection.commit()
        cursor.close()

        tishi = "修改密码成功!"
        return render_template('医生_修改密码.html', tishi=tishi)

    return render_template('医生_修改密码.html')

@app.route('/hz_zy')
def hz():
    patient_name = request.cookies.get('patient_name')
    connection = get_mysql_connection()
    cursor = connection.cursor()

    query2 = 'SELECT 用户名 FROM hz where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (patient_name, patient_name))
    name = cursor.fetchall()[0][0]

    query = 'SELECT * FROM 用药方案提醒 where 患者名称 = %s'
    cursor.execute(query, (name,))
    second = cursor.fetchall()
    if second != []:
        pass
    else:
        insert_query = "INSERT 用药方案提醒 (患者名称, 提醒时间) VALUES (%s,'07:00:00')"
        cursor.execute(insert_query, (patient_name,))

    加载延时用药信息(name)

    connection.commit()
    cursor.close()

    data_points = [15339, 21345, 18483, 24003, 23489, 24092, 12034]
    labels = ['good day', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return render_template('hz_zy.html', data_points=data_points, labels=labels)

@app.route('/hz_xgmm', methods=['GET', 'POST'])
def hz_xgmm():
    if request.method == "POST":
        doctor_name = request.cookies.get('patient_name')
        密码 = request.form.get('密码')
        确认密码 = request.form.get('确认密码')

        if 密码 != 确认密码:
            tishi = "两次密码不一样!"
            return render_template('患者_修改密码.html', tishi=tishi)

        encrypted_data = generate_password_hash(密码)
        connection = get_mysql_connection()
        cursor = connection.cursor()

        query2 = 'SELECT 用户名 FROM hz where 用户名 = %s or 账号 = %s'
        cursor.execute(query2, (doctor_name, doctor_name))
        doctor_name = cursor.fetchall()[0][0]

        insert_query = "UPDATE hz SET 密码=%s WHERE 用户名 = %s"
        cursor.execute(insert_query, (encrypted_data, doctor_name))
        connection.commit()
        cursor.close()
    return render_template('患者_修改密码.html')

@app.route('/hz_ywxx',methods=['GET', 'POST'])
def hz_ywxx():
    #获取数据，以时间段来判断而不是一个药方
    if request.method == "POST":
        实际服用的药物名称 = request.form.get('实际服用的药物名称')
        状态 = request.form.get('状态')
        实际服用时间 = request.form.get('实际服用时间')
        患者名称 = request.form.get('患者名称')
        医生名称 = request.form.get('医生名称')
        计划服药的时间段 = request.form.get('计划服药的时间段')

        connection = get_mysql_connection()
        cursor = connection.cursor()

        #判断时间是否正确
        query3 = 'SELECT * FROM 用药方案 where 医生名称=%s and 患者名称 = %s and 计划服用时间 = %s'
        cursor.execute(query3, (医生名称, 患者名称,计划服药的时间段,))
        ans = cursor.fetchall()
        if ans == []:
            tishi = "计划服药的时间段输入错误!"
            return render_template('患者_用药信息.html',tishi=tishi)

        实际服用的药物名称_列表 = 实际服用的药物名称.split(",")

        #如果只有一个，检查是否存在多个在方案里，进行判断
        if len(实际服用的药物名称_列表) == 1:
            query3 = 'SELECT 用药名称 FROM 用药方案 where 医生名称=%s and 患者名称 = %s and 计划服用时间=%s'
            cursor.execute(query3, (医生名称, 患者名称,计划服药的时间段,))
            ans = cursor.fetchall()

            #如果不是ans 1 就意味着是有药物延期了
            if len(ans) != 1 and ans != []:
                #更新实际服用的药物，延期没有服用的药物
                connection = get_mysql_connection()
                cursor = connection.cursor()
                insert_query = "UPDATE 用药方案 SET 状态=%s,实际服用时间=%s WHERE 用药名称 = %s and 患者名称 = %s and 计划服用时间=%s and 医生名称 = %s"
                cursor.execute(insert_query, (状态, 实际服用时间, 实际服用的药物名称, 患者名称, 计划服药的时间段,医生名称))
                connection.commit()
                cursor.close()
                加载延时用药信息(患者名称)
            elif len(ans) == 1:
                connection = get_mysql_connection()
                cursor = connection.cursor()
                insert_query = "UPDATE 用药方案 SET 状态=%s,实际服用时间=%s WHERE 用药名称 = %s and 患者名称 = %s and 计划服用时间=%s and 医生名称 = %s"
                cursor.execute(insert_query, (状态, 实际服用时间, 实际服用的药物名称, 患者名称, 计划服药的时间段,医生名称))
                connection.commit()
                cursor.close()

        elif len(实际服用的药物名称_列表) >1:
            query3 = 'SELECT 用药名称 FROM 用药方案 where 医生名称=%s and 患者名称 = %s and 计划服用时间=%s and 医生名称 = %s'
            cursor.execute(query3, (医生名称, 患者名称, 计划服药的时间段,医生名称))
            ans = cursor.fetchall()

            if ans != [] and len(ans) != len(实际服用的药物名称_列表):
                for i in 实际服用的药物名称_列表:
                    connection = get_mysql_connection()
                    cursor = connection.cursor()
                    insert_query = "UPDATE 用药方案 SET 状态=%s,实际服用时间=%s WHERE 用药名称 = %s and 患者名称 = %s and 计划服用时间=%s and 医生名称 = %s"
                    cursor.execute(insert_query, (状态, 实际服用时间, i, 患者名称, 计划服药的时间段,医生名称))
                    connection.commit()
                    cursor.close()
                加载延时用药信息(患者名称)
            elif len(ans) == len(实际服用的药物名称_列表):
                for i in 实际服用的药物名称_列表:
                    connection = get_mysql_connection()
                    cursor = connection.cursor()
                    insert_query = "UPDATE 用药方案 SET 状态=%s,实际服用时间=%s WHERE 用药名称 = %s and 患者名称 = %s and 计划服用时间=%s and 医生名称 = %s"
                    cursor.execute(insert_query, (状态, 实际服用时间, i, 患者名称, 计划服药的时间段,医生名称))
                    connection.commit()
                    cursor.close()

        connection.commit()
        cursor.close()

    return render_template('患者_用药信息.html')

@app.route('/患者_用药方案提醒',methods=['GET', 'POST'])
def 患者_用药方案提醒():
    if request.method == "POST":
        patient_name = request.cookies.get('patient_name')
        提醒时间 = request.form.get('提醒时间')
        connection = get_mysql_connection()
        cursor = connection.cursor()

        query = 'SELECT * FROM 用药方案提醒 where 患者名称 = %s'
        cursor.execute(query, (patient_name,))
        second = cursor.fetchall()
        if second != []:
            insert_query = "UPDATE 用药方案提醒 SET 提醒时间=%s WHERE 患者名称 = %s"
            cursor.execute(insert_query, (提醒时间, patient_name))
        else:
            insert_query = "INSERT 用药方案提醒 (患者名称, 提醒时间 VALUES (%s,%s)"
            cursor.execute(insert_query, (patient_name, 提醒时间))
        connection.commit()
        cursor.close()
    return render_template('患者_用药方案提醒.html')



@app.route('/hz_jkda')
def hz_jkda():
    patient_name = request.cookies.get('patient_name')
    connection = get_mysql_connection()
    cursor = connection.cursor()

    query = 'SELECT 健康档案权限 FROM hz where 用户名 = %s or 账号 = %s'
    cursor.execute(query, (patient_name, patient_name))
    second = cursor.fetchall()

    if second[0][0] != "是":
        return render_template('无权访问.html')

    query2 = 'SELECT 用户名 FROM hz where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (patient_name,patient_name))
    name = cursor.fetchall()[0][0]

    query = 'SELECT * FROM 用药方案 where (患者名称 = %s) and (状态 = "完成" or 状态 = "未完成") '
    cursor.execute(query, (name,))
    second = cursor.fetchall()

    unique_values = set()

    # Create a new list to store deduplicated tuples
    deduplicated_data = []

    for item in second:
        value = item[1]  # Get the value from the second column
        if value not in unique_values:
            unique_values.add(value)  # Add the value to the set
            deduplicated_data.append(item)  # Add the tuple to the deduplicated list

    connection.commit()
    cursor.close()
    return render_template('hz_jkda.html',second=second,deduplicated_data=deduplicated_data)

def 加载延时用药信息(patient_name):
    connection = get_mysql_connection()
    cursor = connection.cursor()

    # 这一段主要是判断和推后时间
    query4 = 'SELECT 处方名称,实际服用时间,计划服用时间 FROM 用药方案 where 患者名称 = %s'
    cursor.execute(query4, (patient_name,))
    second2 = cursor.fetchall()

    for i in second2:
        format_str = "%Y-%m-%d %H:%M:%S"

        time1 = datetime.now()

        time_str2 = str(i[2])
        time2 = datetime.strptime(time_str2, format_str)

        now_day = str(time1).split(" ")[0]

        # 判断是在什么时间段内 7-12 12-18 18以后,判断成功之后，改变对应的时间的处方，将时间延长
        if i[1] == "无" and time1 > time2:
            if time1 > datetime.strptime(now_day + " 07:00:00", "%Y-%m-%d %H:%M:%S") and time1 < datetime.strptime(
                    now_day + " 12:00:00", "%Y-%m-%d %H:%M:%S"):
                insert_query2 = "UPDATE 用药方案 SET 计划服用时间=%s WHERE 患者名称 = %s and 处方名称=%s and 计划服用时间=%s"
                cursor.execute(insert_query2, (
                datetime.strptime(now_day + " 12:00:00", "%Y-%m-%d %H:%M:%S"), patient_name, i[0], i[2]))

            elif time1 > datetime.strptime(now_day + " 12:00:00", "%Y-%m-%d %H:%M:%S") and time1 < datetime.strptime(
                    now_day + " 18:00:00", "%Y-%m-%d %H:%M:%S"):
                insert_query3 = "UPDATE 用药方案 SET 计划服用时间=%s WHERE 患者名称 = %s and 处方名称=% and 计划服用时间=%s"
                cursor.execute(insert_query3,
                               (datetime.strptime(now_day + " 18:00:00", "%Y-%m-%d %H:%M:%S"), patient_name, i[0], i[2],))
                print(datetime.strptime(now_day + " 18:00:00", "%Y-%m-%d %H:%M:%S"), patient_name, i[0], i[2])

            elif time1 > datetime.strptime(now_day + " 18:00:00", "%Y-%m-%d %H:%M:%S"):
                insert_query2 = "UPDATE 用药方案 SET 计划服用时间=%s WHERE 患者名称 = %s and 处方名称=%s and 计划服用时间=%s"
                cursor.execute(insert_query2,
                               (
                               datetime.strptime(now_day + " 20:00:00", "%Y-%m-%d %H:%M:%S"), patient_name, i[0], i[2]))

    connection.commit()
    cursor.close()

@app.route('/hz_ywgl',methods=['GET','POST'])
def hz_ywgl():
    patient_name = request.cookies.get('patient_name')

    connection = get_mysql_connection()
    cursor = connection.cursor()

    #获取用户名
    query2 = 'SELECT 用户名 FROM hz where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (patient_name, patient_name))
    name = cursor.fetchall()[0][0]
    #######################################

    #检查是否有权限
    query2 = 'SELECT 用药管理权限 FROM hz where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (patient_name, patient_name))
    second = cursor.fetchall()

    if second[0][0] != "是":
        return render_template('无权访问.html')
    ########################################

    if request.method == "POST":
        药物名称 = request.form.get('药物名称')
        服用时间 = request.form.get('服用时间')
        用药方案名称 = request.form.get('用药方案名称')

        query = 'SELECT * FROM 药物提醒 where 患者名称 = %s and 药物名称 = %s and 用药方案名称 = %s'
        cursor.execute(query, (name,药物名称,用药方案名称))
        second = cursor.fetchall()

        if second != []:
            insert_query3 = "UPDATE 药物提醒 SET 服用时间=%s where 患者名称 = %s and 药物名称 = %s and 用药方案名称 = %s"
            cursor.execute(insert_query3, (服用时间, name,药物名称,用药方案名称))
        else:
            insert_query3 = "INSERT INTO 药物提醒 (患者名称, 药物名称, 用药方案名称, 服用时间) VALUES (%s,%s,%s,%s)"
            cursor.execute(insert_query3, (patient_name, 药物名称,用药方案名称,服用时间))

        connection.commit()
        cursor.close()

    connection.commit()
    cursor.close()

    connection = get_mysql_connection()
    cursor = connection.cursor()

    #这里是将时间当作计划服用时间来计算的，干脆改了 直接得在开具处方的时候就弄好了，这里的是直接获取【药物名称，用药时间】
    query3 = 'SELECT 用药名称,用药计量,时间,处方名称,状态,计划服用时间,实际服用时间 FROM 用药方案 where 患者名称 = %s and ( 状态="未完成" or 状态="完成" )'
    cursor.execute(query3, (name,))
    second = cursor.fetchall()
    target = []
    for i in second:
        target.append([i[0],i[2],i[3],i[4],i[6],i[5]])

    加载延时用药信息(name)

    connection.commit()
    cursor.close()

    prescription_summary = {}


    for prescriptions in target:

        drug_name = prescriptions[0]
        start_time = prescriptions[5]
        处方名称 = prescriptions[2]
        status = prescriptions[3]
        完成时间 = prescriptions[4]

        time_period = f"{start_time}"

        if time_period not in prescription_summary:
            prescription_summary[time_period] = []

        prescription_summary[time_period].append({
                '药物名称': drug_name,
                '完成时间': 完成时间,
                '处方名称': 处方名称,
                '状态': status,
            })


    targets = []
    for time_period, prescriptions in prescription_summary.items():

        药物名称 = ""
        处方名称 = ""
        状态 = ""
        for prescription in prescriptions:
            药物名称 += prescription['药物名称'] + ","
            处方名称 += prescription['处方名称'] + ","
            状态 += prescription['状态'] + ","
        targets.append([time_period, 药物名称, 处方名称, 状态, prescriptions[0]['完成时间']])

    return render_template('hz_ywgl.html',second=targets)

@app.route('/患者_药物提醒',methods=['POST'])
def 患者_药物提醒():

    data = request.get_json()
    处方名称 = data["name1"]
    药物名称 = data["name2"]
    url = url_for('new_page', param1=处方名称, param2=药物名称)
    return redirect(url_for('login'))


@app.route('/hz_pj')
def hz_pj():
    patient_name = request.cookies.get('patient_name')
    connection = get_mysql_connection()
    cursor = connection.cursor()

    query = 'SELECT 评价权限 FROM hz where 用户名 = %s or 账号 = %s'
    cursor.execute(query, (patient_name, patient_name))
    second = cursor.fetchall()
    if second[0][0] != "是":
        return render_template('无权访问.html')

    query2 = 'SELECT 用户名 FROM hz where 用户名 = %s or 账号 = %s'
    cursor.execute(query2, (patient_name, patient_name))
    name = cursor.fetchall()[0][0]

    query1 = 'SELECT 处方名称,状态 FROM 用药方案 where 患者名称 = %s'
    cursor.execute(query1, (name,))
    frist = cursor.fetchall()

    filtered_data = []
    removed_names = set()
    for element in frist:
        if element[1] != '未完成':
            filtered_data.append(element)
        else:
            removed_names.add(element[0])

    final_data = [element for element in filtered_data if element[0] not in removed_names]

    for i in final_data:
        if i[1] == "已完成" or i[1] == "完成":
            query4 = 'SELECT * FROM 评价 where 患者名称 = %s and 处方名称 = %s'
            cursor.execute(query4, (name, i[0]))
            second = cursor.fetchall()
            if second == []:
                insert_query = "INSERT INTO 评价 (患者名称, 评价内容, 处方名称, 评价时间) VALUES (%s,'无',%s,'无')"
                cursor.execute(insert_query, (name, i[0]))
            else:
                print("已录入！",i)
    query3 = 'SELECT * FROM 评价 where 患者名称 = %s'
    cursor.execute(query3, (name,))
    target = cursor.fetchall()
    connection.commit()
    cursor.close()
    return render_template('hz_pj.html',target=target)

@app.route('/患者_修改评价', methods=['GET', 'POST'])
def 患者_修改评价():
    if request.method == "POST":
        patient_name = request.cookies.get('patient_name')

        处方名称 = request.form.get('处方名称')
        评价内容 = request.form.get('评价内容')
        时间 = datetime.now()

        connection = get_mysql_connection()
        cursor = connection.cursor()

        query2 = 'SELECT 用户名 FROM hz where 用户名 = %s or 账号 = %s'
        cursor.execute(query2, (patient_name, patient_name))
        patient_name = cursor.fetchall()[0][0]

        insert_query = "UPDATE 评价 SET 评价内容=%s,评价时间=%s WHERE 患者名称 = %s and 处方名称=%s"
        cursor.execute(insert_query, (评价内容, 时间,patient_name,处方名称))
        connection.commit()
        cursor.close()
    return render_template('患者_修改评价.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        connection = get_mysql_connection()
        cursor = connection.cursor()

        floatingInput = request.form.get('floatingInput2')
        floatingPassword = request.form.get('floatingPassword2')

        if floatingInput == admin_name and floatingPassword == admin_password:
            connection.commit()
            cursor.close()
            #系统_患者用药方案提醒()
            #系统_患者药物提醒()
            return redirect('gly')

    try:
        insert_query1 = "SELECT 密码 FROM ys WHERE (用户名 = %s or 账号 = %s) and 状态='启用' "
        cursor.execute(insert_query1, (floatingInput,floatingInput))
        frist = cursor.fetchall()[0][0]

        if check_password_hash(frist, floatingPassword):
            response = make_response(redirect(url_for('ys')))
            response.set_cookie('doctor_name', floatingInput)
            connection.commit()
            cursor.close()
            #系统_患者用药方案提醒()
            #系统_患者药物提醒()
            return response
    except:
        pass

    try:
        insert_query2 = "SELECT 密码 FROM hz WHERE (用户名 = %s or 账号 = %s) and 状态='启用'"
        cursor.execute(insert_query2, (floatingInput,floatingInput))
        second = cursor.fetchall()[0][0]
        if check_password_hash(second, floatingPassword):
            response = make_response(redirect(url_for('hz')))
            response.set_cookie('patient_name', floatingInput)
            connection.commit()
            cursor.close()
            #系统_患者用药方案提醒()
            #系统_患者药物提醒()
            return response
    except:
        pass

    return render_template('login.html')


if __name__ == '__main__':
    admin_name = "123"
    admin_password = "123"
    app.run(debug=True,port=5007)


