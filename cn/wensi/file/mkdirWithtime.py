#encoding=utf-8

#创建一个目录：年月日.进入这个目录，创建一个当前小时的目录。
# 在进入小时的目录的，创建一个分钟的目录。
# 再进入分钟的目录创建一个文件，当前秒数为文件名，然后文件内容写上年月日时分秒。封装成函数

import time
import os
def mkdir_with_time(path):
    year_month_day = time.strftime("%Y%m%d",time.localtime())
    os.chdir(path)
    os.mkdir(year_month_day)

    os.chdir(os.path.join(path,year_month_day))
    hour = time.strftime("%H",time.localtime())
    os.mkdir(hour)

    os.chdir(os.path.join(os.getcwd(),hour))
    minite = time.strftime("%M",time.localtime())
    os.mkdir(minite)

    os.chdir(os.path.join(os.getcwd(),minite))
    print os.getcwd()
    second = time.strftime("%S",time.localtime())
    with open(os.getcwd()+"\\"+second + ".txt","w") as fp:
        fp.write(time.strftime("%Y%m%d %H:%M:%S",time.localtime()))

mkdir_with_time(r"d:/test")