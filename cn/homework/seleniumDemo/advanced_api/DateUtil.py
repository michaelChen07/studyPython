#encoding=utf-8
import time
from datetime import datetime

'''
本文件主要用于获取当前的日期以及时间，
用于生成保存截图文件目录名
'''

def currentDate():
    date = time.localtime()
    # 构造今天的日期字符串
    today = str(date.tm_year) + "-" + str(date.tm_mon) + "-" + str(date.tm_mday)
    return today

def currentTime():
     timeStr = datetime.now()
     # 构造当前时间字符串
     now = timeStr.strftime('%H-%M-%S')
     return now

if __name__ == "__main__":
    print currentDate()
    print currentTime()
