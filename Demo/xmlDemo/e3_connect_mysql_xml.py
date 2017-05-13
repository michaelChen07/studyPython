#encoding=utf-8
import MySQLdb
from xml.dom.minidom import parse

#minidom解析器打开xml文档并将其解析为内存中的一棵树
DOMTree = parse(r"C:\Users\Administrator\Documents\HBuilderProject\GetStart\xml\e3_mysql.xml")

#获取xml文档对象，就是拿到树的根
mysqlconfig = DOMTree.documentElement

def get_mysqlconfig(arg):
    return mysqlconfig.getElementsByTagName(arg)[0].childNodes[0].data

db_host = get_mysqlconfig("db_host")
db_port = int(get_mysqlconfig("db_port"))
db_user = get_mysqlconfig("db_user")
db_pw = get_mysqlconfig("db_password")
db_base = get_mysqlconfig("db_base")
db_charset = get_mysqlconfig("db_charset")

#打开数据库连接
conn = MySQLdb.connect(
    host = db_host,
    port = db_port,
    user = db_user,
    passwd = db_pw,
    db = db_base,
    charset = db_charset)

# 使用cursor()方法获取数据库的操作游标
cursor = conn.cursor()
cursor.execute("show tables;")
resSet = cursor.fetchall()
print u"共%s条数据。" %len(resSet)
print resSet

#写入excel
from openpyxl import Workbook
wb=Workbook()
ws=wb.active
ws.append(['host','user','password','db'])
ws.append([db_host,db_user,db_pw,db_base])
wb.save('xml.xlsx')