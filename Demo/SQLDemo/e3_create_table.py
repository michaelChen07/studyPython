# coding=utf-8
import MySQLdb

try:
    conn = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="gloryroad"
    )
    conn.select_db('pythondbnew')  # 选择pythonDB数据库
    cur = conn.cursor()  # 获取游标

    # 如果所建表已存在，删除重建
    cur.execute("drop table if exists emp_info;")
    cur.execute("drop table if exists salary;")
    # 执行建表sql语句
    cur.execute('''create table emp_info(
id int not null auto_increment,
name varchar(30) not null,
sex char(4) default null,
dept varchar(10),
mobile varchar(11) not null unique,
birthday date default "0000-00-00",
primary key(id)
)engine=innodb character set utf8 comment 'employer info';''')

    cur.execute('''create table salary(
id int not null auto_increment,
emp_id int not null,
salary int not null,
primary key(id)
)engine=innodb character set utf8 comment 'employer salary info';''')

    cur.close()
    conn.close()
    print u"创建数据表成功"
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
