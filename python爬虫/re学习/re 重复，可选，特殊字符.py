import re

s = "\d{3}[a-z]{3}"
s2 = "[a-z]?\d+"
s3 = "\w*\d+"

list1 = ['123aaa','1233aa','aaaa']
list2 = ['1','aaa11','a11']
list3 = ['123465w','www1','wwwww']

for i in list1:
          m = re.match(s,i)
          if m is not None:
                    print(m.group())
          else:
                    print('不匹配')

for i in list2:
          m = re.match(s2,i)
          if m is not None:
                    print(m.group())
          else:
                    print('不匹配')

#结果是\w\d一起出现时优先后面
for i in list3:
          m = re.match(s3,i)
          if m is not None:
                    print(m.group())
          else:
                    print('不匹配')


