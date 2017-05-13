#coding: utf-8
import multiprocessing
import time
def m1(x):
    time.sleep(0.01)
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    i_list = range(1000)
    time1=time.time()
    pool.map(m1, i_list)
    time2=time.time()
    print 'time elapse:',time2-time1

    time1=time.time()
    map(m1, i_list)
    time2=time.time()
    print 'time elapse:',time2-time1
