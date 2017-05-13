#coding=utf-8

import ConfigParser
import MySQLdb

cf = ConfigParser.ConfigParser()

cf.read("test.ini")

db_host = cf.get("db", "db_host")
db_port = cf.getint("db", "db_port")
db_user = cf.get("db", "db_user")
db_pass = cf.get("db", "db_password")
db_charset = cf.get("db", "db_charset")
db_db = cf.get("db","db_db")
db_sql = cf.get("sql","db_sql")

#打开数据库连接
conn = MySQLdb.connect(
    host = db_host,
    port = db_port,
    user = db_user,
    passwd = db_pass,
    db = db_db,
    charset = db_charset)

#使用cursor()方法获取数据库的操作游标
cursor = conn.cursor()
cursor.execute(db_sql)

#使用fetchall取出所有结果集数据
resSet = cursor.fetchall()
print u"共%s条数据。" %len(resSet)
print resSet
