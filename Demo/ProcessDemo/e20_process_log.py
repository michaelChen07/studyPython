# encoding=utf-8
import multiprocessing
import logging
import sys

def worker():
    print 'I am working....'
    sys.stdout.flush()

if __name__ == '__main__':
    # 设置日志输出到控制台
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    # 设置输出日志的级别
    logger.setLevel(logging.INFO)
    p = multiprocessing.Process(name="gloryroad",target = worker)
    p.start()
    p.join()
