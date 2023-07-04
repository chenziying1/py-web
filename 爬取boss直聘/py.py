import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



smtpserver = "smtp.qq.com"
smtpport = 465
from_mail = "323821829@qq.com"
to_mail = ["1060324818@qq.com"]
password = "tkljkcluknxcbigf"   # 16位授权码


subject = "火车票快没有啦！"
from_name = "去哪儿抢火车票程序"

msg = MIMEMultipart()
msg["Subject"] = Header(subject, "utf-8")
msg["From"] = Header(from_name + " <" + from_mail + ">", "utf-8")
msg["To"] = Header(",".join(to_mail), "utf-8")
body = "你要查询的火车票只剩下不到10张了！"
msgtext = MIMEText(body, "plain", "utf-8")
msg.attach(msgtext)


try:
    smtp = smtplib.SMTP_SSL(smtpserver,smtpport)
    smtp.login(from_mail,password)
    smtp.sendmail(from_mail,to_mail,msg.as_string())
except(smtplib.SMTPException) as e:
    print(e.message)
finally:
    smtp.quit()
