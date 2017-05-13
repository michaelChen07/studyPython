#encoding=utf-8

import time
import os
import datetime
now = datetime.datetime.now()
#nowDate = now.strftime("%Y%m%d")#今年的日期
#thisDate = now.strftime("%j")#今年第X天
#thisweek = now.strftime("%U")#今年第X周
#thisweekday = now.strftime("%w")#今年是周X

thisyear = time.localtime().tm_year
lastyear = datetime.datetime.now().replace(year = thisyear-1)
#lastyearDate = lastyear.strftime("%Y%m%d")#去年今天的日期
#lastDate = lastyear.strftime("%j")#去年第X天
#lastWeek = lastyear.strftime("%U")#去年第X周
#lastWeekday = lastyear.strftime("%w")#去年是周X

oneYearAfter = datetime.datetime.now().replace(year = thisyear+1)
#oneYearAfterDate = oneYearAfter.strftime("%Y%m%d")#明年今天的日期
#AfterDate = oneYearAfter.strftime("%j")#明年第X天
#AfterWeek = oneYearAfter.strftime("%U")#明年第X周
#AfterWeekday = oneYearAfter.strftime("%w")#明年是周X

def creat_log_with_time(path):
    os.chdir(path)
    os.mkdir("log")
    os.chdir("log")
    dir_list = [lastyear,now,oneYearAfter]
    for i in dir_list:
        os.mkdir(i.strftime("%Y%m%d"))#日期
        os.chdir(i.strftime("%Y%m%d"))
        with open(i.strftime("%j")+".log","w") as fp:
            content = "当年的今天是这一年的第%s个星期,当前是星期%s"%(i.strftime("%U"),i.strftime("%w"))
            fp.write(content)
        os.chdir(os.path.join(path,"log"))
    return "sucess"

print creat_log_with_time(r"d:\test")