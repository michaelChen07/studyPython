#encoding=utf-8

#多线程并发，性能测试程序：

from multiprocessing import Manager, Pool, cpu_count
from multiprocessing.managers import BaseManager
import MySQLdb
import os, random, traceback


# 创建数据库，创建表
def createTable():
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="gloryroad")

    cur = conn.cursor()
    sql_database = 'CREATE DATABASE IF NOT EXISTS userinfo DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
    sql_table = '''create table student(
      ID int not null auto_increment comment "不为空的自增长的主键ID",
      name varchar(30) not null,
      age int default 0,
      email varchar(40),
      tel varchar(13) unique not null,
      primary key (ID)
    )engine=innodb character set utf8 comment "表注释";'''

    try:
        # 建库
        cur.execute(sql_database)
        conn.select_db('userinfo')
        cur.execute("drop table if exists student;")
        # 建表
        cur.execute(sql_table)
    except Exception, e:
        print e
    else:
        print u"数据库及数据表创建成功！"
        cur.close()
        conn.commit()
        conn.close()


class myMySQL(object):
    def __init__(self):
        # 打开数据库连接
        self.conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="gloryroad",
            db="userinfo",
            charset="utf8")
        # 使用cursor()方法获取数据库的操作游标
        self.cur = self.conn.cursor()

    def executeSql(self, sql):
        print sql
        try:
            res = self.cur.execute(sql)
            print "sql end ", res
            self.conn.commit()
        except:
            traceback.print_exc()

    def quit(self):
        print "quit===="
        self.cur.close()
        self.conn.commit()
        self.conn.close()


class MyManager(BaseManager): pass


def my_Manager():
    m = MyManager()
    m.start()
    return m


# 将myMySQL类注册到MyManager管理类中
MyManager.register('myMySQL', myMySQL)


# print "----", MyManager.__dict__

def run(my_sql):
    print "subprocesses is", os.getpid()
    # 造数据
    name = 'Amy' + str(random.randint(1, 100)) + '_' + str(os.getpid())
    age = random.randint(1, 100)
    email = name + '@qq.com'
    tel = '1' + str(random.choice([3, 5, 7, 8])) + str(random.random())[2:11]
    sql = 'insert into student(name, age, email, tel) values("%s", "%s", "%s", "%s")' % (name, age, email, tel)
    # 插入数据
    my_sql.executeSql(sql)


if __name__ == '__main__':
    createTable()
    # 创建进程共享数据对象
    manager = my_Manager()
    # 因为myMySQL类注册到MyManager管理类中，所以可以使用如下语句创建共享对象中的myMySQL实例对象，在不同进程间调用
    my_sql = manager.myMySQL()
    # print "111", my_sql
    print 'Parent process %s.' % os.getpid()
    p = Pool(cpu_count())
    n = 100
    while n:
        p.apply(run, args=(my_sql,))  # 每调用一次此方法会生成一个进程，最多生成和cpu盒数相当的进程
        n -= 1
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
    my_sql.quit()
