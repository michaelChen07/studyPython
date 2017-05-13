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