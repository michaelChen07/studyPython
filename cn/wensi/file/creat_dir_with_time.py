#encoding=utf-8

#从命令行接受1个路径如：c:\a\b\c\1.py, 实现1个函数创建目录a\b\c,创建文件1.py ，实现1个函数删除已创建的目录及文件
import os
file_path = "d:\\test\\test2\\test3\\1.py"

def del_dir(path):
    #os.remove(file_path)
    dirpath = os.path.splitdrive(file_path)[0]
    os.chdir(dirpath+"\\")
    return os.listdir(os.getcwd())

print del_dir(file_path)


#创建三级目录，一级目录名是去年的月份，二级目录名是上个月的月份，三级目录是今天的日期。
#三级目录下，创建文件名是现在的时分秒，写入内容：今天是今年的第%s天，今年的第%s个星期
import time
import os
import datetime
def creat_dirwithtime(path):
    os.chdir(path)

    #去年的年份
    lastyear = datetime.datetime.now().year - 1
    os.mkdir(str(lastyear))
    os.chdir(os.path.join(os.getcwd(),str(lastyear)))

    #上个月的月份
    month = datetime.datetime.now().month - 1
    if month < 1:
        month =+ 12
    os.mkdir(str(month))
    os.chdir(os.path.join(os.getcwd(), str(month)))

    #今天的日期
    todaydate = datetime.datetime.now().day
    os.mkdir(str(todaydate))
    os.chdir(os.path.join(os.getcwd(),str(todaydate)))

    #当前时分秒
    nowtime = time.strftime("%H%M%S",time.localtime())

    now = datetime.datetime.now()
    datecount = now.strftime("%j")#今天是今年的第X天
    weekcount = now.strftime("%U")#今天是今年的第X周
    with open(nowtime+".txt","w") as fp:
        content = "今天是今年的第%s天，今年的第%s个星期"%(datecount,weekcount)#文件写入的内容
        fp.write(content)
    return "done"

print creat_dirwithtime(r"d:\test")




