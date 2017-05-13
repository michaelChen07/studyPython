# encoding=utf-8
import multiprocessing


def do(n) :
    # 获取当前线程的名字
    name = multiprocessing.current_process().name
    print name,'starting'
    print "worker ", n
    return

if __name__ == '__main__' :
    numList = []
    for i in xrange(5) :
        p = multiprocessing.Process(target=do, args=(i,))
        numList.append(p)
        p.start()
        print numList
        p.join()
        print "Process end."
    print numList
