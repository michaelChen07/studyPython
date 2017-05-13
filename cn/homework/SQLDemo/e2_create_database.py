#coding=utf-8
import MySQLdb

#打开数据库连接
conn = MySQLdb.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    passwd = "gloryroad",
    db = "gloryroad",
    charset = "utf8")

# 使用cursor()方法获取数据库的操作游标
cursor = conn.cursor()
print cursor
print type(cursor)

#创建数据库
#coding=utf-8
import MySQLdb
try:
    conn = MySQLdb.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    passwd = "gloryroad"
    )
    cur = conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS pythonDBnew DEFAULT CHARSET utf8 COLLATE utf8_general_ci;')
    cur.close()
    conn.close()
    print u"创建数据库pythonDB成功! "
except MySQLdb.Error, e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
