# encoding=utf-8
from multiprocessing import Process, Queue
import random
import os

def offer1(queue):
  # 入队列
  queue.put("Hello World")

if __name__ == '__main__':
    # 创建一个队列实例
    q = Queue()
    p = Process(target = offer1, args = (q,))
    p.start()
    print q.get() # 出队列
    p.join()




def offer(queue,content):
    # 入队列
    print "pid:%s,write %s" %(os.getpid(),content)
    queue.put(content)

if __name__ == '__main__':
    process_list=[]
    q = Queue()
    for i in range(5):
        process_list.append(Process(target = offer, args = (q,str(random.randint(1,100)),)))
        process_list[i].start()
        process_list[i].join()
        print "pid:%s,read %s" %(os.getpid(),q.get()) # 出队列
    print q.get()



