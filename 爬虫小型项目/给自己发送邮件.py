import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="czy123007"    #用户名
mail_pass="czy13229539388"   #口令 
 
 
sender = 'czy123007@163.com'
receivers = ['1060324818@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 

print("1")
smtpObj = smtplib.SMTP()
print("1")
smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
print("1")
smtpObj.login(mail_user,mail_pass)
print("1")
smtpObj.sendmail(sender, receivers, message.as_string())
print ("邮件发送成功")
