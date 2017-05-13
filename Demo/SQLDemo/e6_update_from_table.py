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

# 更新一条数据
update = cursor.execute("update salary set salary = '100' where salary ='1000'")
print u"修改语句受影响的行数：", update
#查询一条数据
cursor.execute("select * from salary where salary='100';")
print cursor.fetchone()

#批量更新数据
cursor.executemany("update salary set salary = %s where salary=%s", [(200, 2000), (300, 3000)])
# 查看更新后的结果
query = cursor.execute("select * from salary")
print u"表中所有数据："
for i in cursor.fetchall():
    print i


# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
