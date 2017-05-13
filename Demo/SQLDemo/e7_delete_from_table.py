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
print u"表中所有数据："
for i in cursor.fetchall():
    print i

# 删除数据
delete = cursor.execute("delete from salary where salary = 100")
print u"删除语句影响的行数：", delete

print u"删除一条数据后，表中数据："
cursor.execute("select * from salary")
for i in cursor.fetchall():
    print i

# 批量删除数据
delete = cursor.executemany("delete from salary where salary = %s", [(4000), (200,), (300)])
print u"删除语句影响的行数：", delete

print u"删除一条数据后，表中数据："
cursor.execute("select * from salary")
for i in cursor.fetchall():
    print i

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
