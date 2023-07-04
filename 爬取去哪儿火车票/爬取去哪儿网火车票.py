import requests
import re
import json
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_data(url):
          
          headers = {
                    'referer': 'https://train.qunar.com/stationToStation.htm?fromStation=%E6%B9%9B%E6%B1%9F&toStation=%E9%87%8D%E5%BA%86%E8%A5%BF&date=2022-08-25',
                    'cookie':'QN1=00009180306c45e0c6e00d50; QN300=s=bing; QN99=4874; QunarGlobal=10.67.198.14_-27015f5e_182cdba4d10_-56d8|1661309660804; qunar-assist={"version":"20211215173359.925","show":false,"audio":false,"speed":"middle","zomm":1,"cursor":false,"pointer":false,"bigtext":false,"overead":false,"readscreen":false,"theme":"default"}; QN205=s=bing; QN277=s=bing; QN601=c628a8178b638339180b85731f6d7f78; QN163=0; QN48=tc_a030aa03e5457e27_182cdc5d1a4_c0ad; QN269=12D81A40235811ED81FBFA163EFD983B; fid=785c1f83-0a7a-4f56-b987-4e0e9de4ceb5; ariaDefaultTheme=null; ctt_june=1654604625968##iK3wWsXmWhPwawPwasiGW=WRasTTESHDEKvmW2a+EPPnaDjsX2WDaKvnWK28iK3siK3saKjOaKanaS2sWRDsWwPwaUvt; QN271AC=register_pc; QN271SL=6b4c64442f589181d69e1d1040e3fe4a; QN271RC=6b4c64442f589181d69e1d1040e3fe4a; ctf_june=1654604625968##iK3wWSvNWuPwawPwasoDEDfRaKiGWDiDXStnEKj8a23sVRtOE2iIVPfGVR3NiK3siK3saKjOaKanasPsWRasahPwaUvt; cs_june=83f2cda4e32b906239229c8ade4c28d6e39b2eac9e348a3ab225d6d65a68bdd473e0a9c4392ac2c6790fba3627f3fc7e9eed0d9092e84fd294d0488b91deb069b17c80df7eee7c02a9c1a6a5b97c11797be467c9e5856fa8d57eae5cbbe64b985a737ae180251ef5be23400b098dd8ca; _q=U.qunar_lbs_1830391930; csrfToken=PzpccrYPRoLsUrZpUhiU42atlpeYBXfG; _s=s_EK6K2GJIT73IZJZMAXUQMLBRJY; _t=27797998; _v=ENkoRdLa1T16aA_GZyo8nwghvElQPXC5P32kYrIrhy2mzejZ3za8jJD7o7xFZUqPHnQK78XUFzUCzd_QaaE3m3424p1wlnYefmfXbVx7ObmMzz0uUlKuE-0ftXUbq5HqGxBu3gK1J1kVNechsMsrwTUKvqL9OFLTYmmSwpJrrCVR; QN43=""; QN42=%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7; QN44=qunar_lbs_1830391930; _i=DFiEuMRwwwAw_WRetd1w1I8PM1vw; _vi=0QQZYL0_uFf9yVN1YcttivZHSQDdkNUnh0fJK_VTaEF5VtD0MXklesN69LNBj3ziKoRDfJEbg7k3CFX3WiR5Hqbsl--4Tqw6n2INW97i-RUAm4SOzJcEUP6NusDpAQY-Cv-O15g070kB2Z49GqEw1u18lSMYYOah0VCMbK6vCOww; QN271=5115fbfb-e24b-4480-a96e-c9df7d7bd286; RT=s=1661327333333&r=https://train.qunar.com/; QN267=257905267bbf4a56e',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
                    }
          html = requests.get(url,headers = headers)
          html.encoding = 'utf-8'
          strs = html.text
          strs = strs.replace(strs[:45],'')
          strs = strs.replace(');','')
          data = json.loads(strs)
          s2sBeanList = data['data']['s2sBeanList']
          return s2sBeanList

def save(s2sBeanList):
          f = open('numbers.csv', 'w+')
          fnames = ['车次/类型','出发时间','到达时间','经过时间','正常票价','学生票价','剩余票量']
          writer = csv.DictWriter(f, fieldnames=fnames)
          writer.writeheader()


          for i in s2sBeanList:
                    try:
                              price=i['seats']['硬卧']['price']
                              studentPrice=i['seats']['硬卧']['studentPrice']
                              ticketed=i['seats']['硬卧']['count']
                              start_time = i['dptTime']
                              end_time = i['arrTime']
                              duration_time = i['extraBeanMap']['interval']
                              train = i['trainNo']

                              if ticketed < 10:
                                        SMTP()

                              dicts = {
                                        '车次/类型':train,
                                        '出发时间':start_time,
                                        '到达时间':end_time,
                                        '经过时间':duration_time,
                                        '正常票价':price,
                                        '学生票价':studentPrice,
                                        '剩余票量':ticketed,
                                        }
                              writer.writerow(dicts)
                              print('成功存入一条数据!')
                    except:
                              pass

          f.close()

def SMTP():
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
                    

urls = 'https://train.qunar.com/dict/open/s2s.do?callback=jQuery17205812356133612233_1661327333872&dptStation=%E6%B9%9B%E6%B1%9F&arrStation=%E9%87%8D%E5%BA%86%E8%A5%BF&date=2022-08-25&type=normal&user=neibu&source=site&start=1&num=500&sort=3&_=1661327334331'
s2sBeanList = get_data(urls)
save(s2sBeanList)





          

