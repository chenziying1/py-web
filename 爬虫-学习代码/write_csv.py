import csv

with open('data.csv','w',encoding = 'utf-8') as f:
          writer = csv.writer(f)
          writer.writerow(['czy','0001',9999])
          writer.writerow(['czy2','0002',9998])
          
with open('data2.csv','w',encoding = 'gbk') as f:
          filenames = ['名字','工资','年龄']
          writer = csv.DictWriter(f,fieldnames=filenames)
          writer.writeheader()
          writer.writerow({'名字':'czy','工资':2000,'年龄':20})
          writer.writerow({'名字':'czy2','工资':2500,'年龄':20})
          writer.writerow({'名字':'czy3','工资':3000,'年龄':20})
