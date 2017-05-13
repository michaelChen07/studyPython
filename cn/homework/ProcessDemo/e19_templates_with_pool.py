# coding=utf-8
__author__ = 'foster_wu'

from multiprocessing import Pool, Value, Lock, Manager
import os, time, random

def long_time_task(name,requestCount,countList):
    requestCount.value += 1
    print u"计数：", requestCount.value
    countList.append(requestCount.value)
    time.sleep(0.2)
    print 'Run task %s (%s)...\n' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    manager = Manager()
    requestCount = manager.Value('i',0)
    countList = manager.list([])
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args = (str(i),requestCount,countList))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
    print requestCount.value
    print countList
