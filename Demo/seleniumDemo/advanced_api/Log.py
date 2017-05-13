#encoding=utf-8
import logging.config
import logging

logging.config.fileConfig("Logger.conf")

def debug(message):
    # 打印debug级别的日志方法
   print "debug"
   logging.debug(message)

def warning(message):
    # 打印warning级别的日志方法
    logging.warning(message)

def info(message):
    # 打印info级别的日志方法
    logging.info(message)

if __name__=="__main__":
    debug("hi")
