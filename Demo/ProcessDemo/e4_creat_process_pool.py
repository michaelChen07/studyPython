#encoding=utf-8
from multiprocessing import Pool
import time
import random
import os

def f(x):
    #time.sleep(2)
    return x * x

if __name__ == '__main__':
    pool = Pool(processes = 4)      # start 4 worker processes

    #同步串行执行，异步可同时执行。此处result是异步执行
    result = pool.apply_async(f, [10])  # evaluate "f(10)" asynchronously
    # prints "100" unless your computer is *very* slow
    print result.get(timeout = 1)
    print pool.map(f, range(10))   # prints "[0, 1, 4,..., 81]"

    result2 = pool.apply(f, [10])
    print "同步：", result2


def g(x):
    time.sleep(1)
    y=x * x*random.random()
    print "pid:",os.getpid(),y
    time.sleep(random.random()*1)
    return y

if __name__ == '__main__':
    pool = Pool(processes = 4)      # start 4 worker processes
    result1 = pool.apply_async(g, [10])  # evaluate "f(10)" asynchronously
    result2 = pool.apply_async(g, [10])
    result3 = pool.apply_async(g, [10])
    result4 = pool.apply_async(g, [10])
    result5 = pool.apply_async(g, [10])
    print result5.get(timeout = 10)
