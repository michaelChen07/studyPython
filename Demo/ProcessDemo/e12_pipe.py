# encoding=utf-8

import multiprocessing as mp

def proc_1(pipe):
    pipe.send('hello')
    print 'proc_1 received: %s' %pipe.recv()
    pipe.send("what is your name?")
    print 'proc_1 received: %s' %pipe.recv()

def proc_2(pipe):
    print 'proc_2 received: %s' %pipe.recv()
    pipe.send('hello, too')
    print 'proc_2 received: %s' %pipe.recv()
    pipe.send("I don't tell you!")

if __name__ == '__main__':
  # 创建一个管道对象pipe
    pipe = mp.Pipe()
    print len(pipe)
    print type(pipe)
    # 将第一个pipe对象传给进程1
    p1 = mp.Process(target = proc_1, args = (pipe[0], ))
    # 将第二个pipe对象传给进程2
    p2 = mp.Process(target = proc_2, args = (pipe[1], ))
    p2.start()
    p1.start()
    p2.join()
    p1.join()
