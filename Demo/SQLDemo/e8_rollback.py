#encoding=utf-8

import MySQLdb

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
cursor.execute("select * from salary")
datas = cursor.fetchall()
print u"修改前的数据：\n", datas[0]

# 更新数据表中第一条数据
cursor.execute("update salary set salary = 500 where salary = 5000")
cursor.execute("select * from salary")
datas = cursor.fetchall()
print u"修改后的数据：\n", datas[0]

# 回滚事务,在commit后再回滚则无效
conn.rollback()
cursor.execute("select * from salary")
datas = cursor.fetchall()
print u"事务回滚后的数据：\n", datas[0]

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
