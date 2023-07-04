# -*- coding: utf-8 -*-
# time:2023/4/30 9:45
# file 4.30.8.py
# outhor:czy
# email:1060324818@qq.com
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup

#18594287287@163.com
#C**1**8

#FRSIQEBPEHBNGCCR 成功开启IMAP/SMTP服务，在第三方客户端登录时，登录密码输入以下授权密码

def send_email():
    rq = time.strftime("%Y-%m-%d")
    from_addr = "18594287287@163.com"
    smtpserver = "smtp.163.com"
    password = "FRSIQEBPEHBNGCCR"
    to_addr = "1060324818@qq.com"
    subject = "{rq} 微博热搜".format(rq=rq)
    data = analy_html()
    table = "<table>"
    for item in data:
        table += "<tr><td>{order}:{title}:{readers}:{level}</td></tr>".format(
            order=item[0], title=item[1], readers=item[2], level=item[3])
    table += "</table>"
    content = table
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)

    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())
    smtp.quit()
    print("发送完毕")


def get_html():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Referer": "https://www.baidu.com",
        "cookie": "SUB=_2AkMTC4bOf8NxqwJRmfgWzmrmZY9_yAHEieKlV3cVJRMxHRl-yT9kqmAStRB6OIuoITZyqtC40ITZEC0ABO2fr4n5ZCCX; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhgRrHT.GBpdcLRE8G8AbkU; SINAGLOBAL=2005085045921.2822.1683425787602; _s_tentry=-; Apache=4828330584597.535.1683426984581; ULV=1683426984600:2:2:2:4828330584597.535.1683426984581:1683425787617"
    }
    res = requests.get("https://s.weibo.com/top/summary", headers=headers)
    return res.text

def analy_html():
    html = get_html()
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find(name="tbody")
    items = data.find_all(name='tr')
    send_msgs = []
    for item in items:
        order_number = item.find(attrs={"class": "td-01"}).text
        if order_number == "":
            order_number = 0
        title_content = item.find(attrs={"class": "td-02"}).contents
        # 标题
        title = ""
        # 阅读量
        readers = ""
        if len(title_content) > 3:
            print(title_content)
            title = title_content[1].text
            readers = title_content[3].text
        else:
            title = title_content[1].text
            readers = "0"
            # 热度标签
        level = item.find(attrs={"class": "td-03"}).text  # 热度标签
        print(order_number, title, readers, level)
        send_msgs.append((order_number, title, readers, level))
    return send_msgs

if __name__ == "__main__":
    send_email()