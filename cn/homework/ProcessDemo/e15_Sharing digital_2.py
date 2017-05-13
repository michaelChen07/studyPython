# encoding=utf-8
import time
from multiprocessing import Process, Value, Lock

class Counter(object):
    def __init__(self, initval = 0):
        self.val = Value('i', initval)
        self.lock = Lock() # 加锁，去掉锁后值会有影响

    def increment(self):
        with self.lock:
            self.val.value += 1 # 共享变量自加1

    def value(self):
        with self.lock:
            return self.val.value

def func(counter):
    for i in range(50):
        time.sleep(0.01)
        counter.increment()

if __name__ == '__main__':
    counter = Counter(0)
    procs = [Process(target = func, args = (counter,)) for i in range(10)] #10个进程，每个进程执行50次，总计500
    # 等价于
    # for i in range(10):
      # Process(target = func, args = (counter,))
    for p in procs: p.start()
    for p in procs: p.join()
    print counter.value()
