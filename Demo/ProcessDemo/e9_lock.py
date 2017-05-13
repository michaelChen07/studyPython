# encoding=utf-8

from multiprocessing import Process, Lock
import time

def l(num,lock):
    lock.acquire() # 获得锁
    time.sleep(0.2)
    print "Hello Num: %s" % (num)
    lock.release() # 释放锁

if __name__ == '__main__':
    lock = Lock() # 创建一个共享锁实例
    for num in range(50):
        Process(target = l, args = (num,lock)).start()



