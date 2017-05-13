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

#使用cursor()方法获取数据库的操作游标
cursor = conn.cursor()
cursor.execute("select * from emp_info")
"""while 1:
    res = cursor.fetchone()
    if res is None:
    # 表示已经取完结果集
        break
    print res
    #将读取到的时间格式化
    print res[-1].strftime("%Y-%m-%d")"""

#使用fetchmany,获取游标处两条数据
resTuple = cursor.fetchmany(2)
print u"结果集类型：", type(resTuple)
for i in resTuple:
  print i

#使用fetchall取出所有结果集数据
resSet = cursor.fetchall()
print u"共%s条数据。" %len(resSet)
print resSet

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()
print u"sql语句执行成功！"
