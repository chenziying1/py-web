import sqlite3
import os

dbpath = 'data.sqlite'

if not os.path.exists(dbpath):
          conn = sqlite3.connect(dbpath)
          c = conn.cursor()
          c.execute('''CREATE TABLE persons (id int primary key not null,
                    name text not null,
                    age int not null,
                    address char(50),
                    salary real);''')
          conn.commit()
          conn.close()
          print('创建数据库成功！')


conn = sqlite3.connect(dbpath)
c = conn.cursor()
c.execute('delete from persons')
c.execute("insert into persons (id,name,age,address,salary) values (1,'czy',32,'chinese',2000.0)");
c.execute("insert into persons (id,name,age,address,salary) values (2,'czy2',33,'chinese2',2500.0)");
c.execute("insert into persons (id,name,age,address,salary) values (3,'czy3',34,'chinese3',3000.0)");
c.execute("insert into persons (id,name,age,address,salary) values (4,'czy4',35,'chinese4',3500.0)");

conn.commit()
print('插入数据成功!')

persons2 = c.execute('select name,age,address,salary from persons order by age')
result = []
for person in persons2:
          value = {}
          value['name'] = person[0]
          value['age']=person[1]
          value['address']=person[2]
          result.append(value)
conn.close()
print(result)
