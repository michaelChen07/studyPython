#encoding=utf-8
import MySQLdb
import random

def creat_data():
    # 在MySQL 5.7.6版本之后，导入文件只能在secure_file_priv指定的文件夹下。否则报错ERROR 1290 (HY000):
    # 可用show variables like '%secure%';命令显示文件目录，本机是在C:\ProgramData\MySQL\MySQL Server 5.6\Uploads
    filepath = r"C:\ProgramData\MySQL\MySQL Server 5.6\Uploads\insertUserInfo.txt"

    #定义数据量
    count=100000

    #打开文件，并动态生成数据，将数据存在文件中
    try:
        #wb:以二进制格式打开一个文件，只用于写入，如果该文件已存在则将其覆盖，如果该文件不存在，创建新文件
        with open(filepath,"wb") as f:
            for i in range(1,count+1):
                #定义数据，以下只是测试数据，可以根据自己的业务通过调用函数去随机生成对应的值
                id = str(i)
                name=''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',4)).replace('','')
                sex=str(random.choice(['男', '女']))
                age=str(random.randrange(10, 99))
                address=str(random.choice(['北京', '上海','深圳','广州','杭州']))
                telephone=str(random.randint(186000000001,187000000001))
                userInfo = '>'+id+','+name+','+sex+','+age+','+address+','+telephone+'\n'
                f.write(userInfo)
    except Exception,e:
        print Exception,":",e

#创建表格
def creat_table():
    conn = MySQLdb.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    passwd = "gloryroad" ,
    db = "pythondbnew",
    charset = "utf8")

    # 使用cursor()方法获取数据库的操作游标
    cursor = conn.cursor()

    #创建表格t_user
    cursor.execute('''create table t_user(
    id int not null auto_increment,
    name varchar(30) not null,
    sex char(4) default null,
    age int not null,
    address varchar(10),
    telphone varchar(20) not null,
    primary key(id)
    )engine=innodb character set utf8 comment 't_user';''')

    # 提交事务
    conn.commit()
    print u"sql语句执行成功！"

    #在mysql中执行下列sql(目前只能在mysql中执行，python执行报错)
    sql = """LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 5.6\\Uploads\\insertUserInfo.txt' INTO TABLE t_user
          FIELDS TERMINATED BY '\,' OPTIONALLY ENCLOSED BY '\"' LINES STARTING BY '\>' TERMINATED BY '\n';"""
    cursor.execute(sql)

    # 提交事务
    conn.commit()


if __name__=="__main__":
    creat_data()
    #creat_table()