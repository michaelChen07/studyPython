#encoding=utf-8
import multiprocessing
import time, logging
import sys

def daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush() # 将缓冲区数据写入终端
    # time.sleep(5)
    print 'Exiting :', p.name, p.pid
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    print 'Exiting :', p.name, p.pid
    sys.stdout.flush()

if __name__ == '__main__':
    # 设置日志输出到控制台
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    # 设置输出日志的级别
    logger.setLevel(logging.DEBUG)

    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True
    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False
    d.start()
    time.sleep(1)
    n.start()
    # d.join()
    # n.join()
    print 'd.is_alive()', d.is_alive()
    print "n.is_alive()", n.is_alive()
    print "main Process end!"
