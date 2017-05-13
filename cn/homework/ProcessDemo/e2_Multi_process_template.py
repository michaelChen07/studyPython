# coding=utf-8
import multiprocessing
import urllib2
import time


def func1(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print html[0:20]
    time.sleep(20)


def func2(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print html[0:20]
    time.sleep(20)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=func1, args=("http://www.sogou.com",), name="gloryroad1")
    p2 = multiprocessing.Process(target=func2, args=("http://www.baidu.com",), name="gloryroad2")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    time.sleep(10)
    print "done!"
