#coding=utf-8
import MySQLdb
import random
import time

conn = MySQLdb.connect(
host = "127.0.0.1",
port = 3306,
user = "root",
passwd = "gloryroad" ,
db = "pythondbnew",
charset = "utf8"
)
# 使用cursor()方法获取数据库的操作游标
cursor = conn.cursor()

#method1：插入一条数据
insert = cursor.execute('''insert into emp_info (name,sex,dept,mobile,birthday)\
values("jason","male","hr","13911056507",now()),\
("foseter","male","dev","13911056501",now()),\
("strong","male","dev","13911056502",now()),\
("curry","male","hr","13911056503",now()),\
("james","male","hr","13911056504",now()),\
("lily","fm","hr","13911056505",now()),\
("jane","fm","account","13911056506",now()),\
("shely","fm","account","13911056508",now()),\
("mcdona","fm","account","13911056509",now()),\
("mary","fm","account","13911056510",now());''')

print u"添加语句受影响的行数：", insert

#method2：通过格式字符串传入值，此方式可以防止sql注入，一次只能插入一条
sql = "insert into salary (emp_id,salary) values(%s, %s)"
cursor.execute(sql, (1,1000))

#可用遍历的方法插入多条
list_insert = [(2,2000),(3,3000),(4,4000),(5,5000),(6,6000),(7,7000),(8,8000),(9,9000),(10,10000)]
for i in list_insert:
    cursor.execute(sql, i)

#method3：类似method2，但可批量插入多条数据
sql = "insert into user values(%s, %s, %s, %s)"
insert = cursor.executemany(sql, [
    (5,'tom','tom','1989-03-17'),
    (6,'amy','test','1898-12-01'),
    (7,'lily','linux','1994-06-23')])
print u"批量插入返回受影响的行数：", insert


#插入当前时间
def now():
    return time.strftime("%Y-%m-%d")

for i in range(10,20):
    #随机插入数据
    sql = "insert into user values(%s, %s, %s, %s)"
    cursor.execute(sql, (random.randint(1,10000),'lucy'+str(random.randint(1,10000)),'efg'+str(random.randint(1,10000)),now()))

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"

