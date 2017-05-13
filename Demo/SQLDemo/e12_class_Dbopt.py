#encoding=utf-8
# coding=utf-8
import ConfigParser
import os
import MySQLdb

#读取配置文件
def read_db_config_file(config_file_path):
    cf = ConfigParser.ConfigParser()
    cf.read("test.ini")
    config_dict = {}
    config_dict["db_host"] = cf.get("db", "db_host")
    config_dict["db_port"] = cf.getint("db", "db_port")
    config_dict["db_user"] = cf.get("db", "db_user")
    config_dict["db_password"] = cf.get("db", "db_password")
    config_dict["db_base"] = cf.get("db", "db_base")
    config_dict["db_charset"] = cf.get("db", "db_charset")
    return config_dict


class DbOpt(object):
    #连接数据库
    def __init__(self, config_file_path):
        config_items = read_db_config_file(config_file_path)
        host = config_items["db_host"]
        port = config_items["db_port"]
        user = config_items["db_user"]
        passwd = config_items["db_password"]
        base = config_items["db_base"]
        db = config_items["db_base"]
        charset = config_items["db_charset"]
        self.conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset
        )

    ## 使用cursor()方法获取数据库的操作游标
    def get_cursor(self):
        return self.conn.cursor()

    #用sql查询数据库
    def query(self, sql):
        self.cursor = self.get_cursor()
        self.cursor.execute(sql)
        resSet = self.cursor.fetchall()
        print len(resSet)
        print resSet

    #插入数据,所有用sql可以完成的操作，都可以调用此函数
    def insert(self, sql):
        self.cursor = self.get_cursor()
        self.cursor.execute(sql)
        self.conn.commit()

    #关闭数据库连接
    def close(self):
        if self.cursor is None:
            pass
        else:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def create_table(self,sql):
        self.cursor = self.get_cursor()
        self.cursor.execute(sql)
        self.conn.commit()

if __name__=="__main__":
    db_ojb = DbOpt("test.ini")
    print db_ojb.get_cursor()
    # print read_db_config_file("test.ini")
    db_ojb.query("select * from salary limit 1;")
    #db_ojb.insert("insert into salary values(1,1,1000);")
    db_ojb.create_table("CREATE TABLE `workers_info` (\
`id` int(11) NOT NULL AUTO_INCREMENT,\
`workername` varchar(20) NOT NULL,\
`sex` enum('F','M','S') DEFAULT NULL,\
`salary` int(11) DEFAULT '0',\
`email` varchar(30) DEFAULT NULL,\
`EmployedDates` date DEFAULT NULL,\
 `department` varchar(30) DEFAULT NULL,\
 PRIMARY KEY (`id`)\
 ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;")
    db_ojb.close()


