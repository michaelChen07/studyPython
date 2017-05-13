# encoding=utf-8
import time, os
import random
from multiprocessing import Pool, Value, Lock
from multiprocessing.managers import BaseManager


class MyManager(BaseManager): # 重新定义了一个类可能是怕破坏BaseManager类的原始性
    pass


def Manager():
    m = MyManager()
    m.start()
    return m


class Counter(object):
    def __init__(self, initval=0):
        self.val = Value('i', initval)
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.val.value += 1

    def value(self):
        with self.lock:
            return self.val.value


# 将Counter类注册到Manager管理类中
MyManager.register('Counter', Counter)


def long_time_task(name, counter):
    time.sleep(0.2)
    print 'Run task %s (%s)...\n' % (name, os.getpid())
    start = time.time()
    # time.sleep(random.random() * 3)
    for i in range(50):
        time.sleep(0.01)
        counter.increment()
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    manager = Manager()

    # 创建共享Counter类实例对象的变量，Counter类的初始值0
    counter = manager.Counter(0)
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(str(i), counter))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
    print counter.value()
