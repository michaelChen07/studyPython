#encoding=utf-8
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    time.sleep(1)
    while not q.empty():
        # if not q.empty():
        print 'Get %s from queue.' % q.get(True)
        time.sleep(1) # 目的是等待写队列完成
if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    pr.join()
