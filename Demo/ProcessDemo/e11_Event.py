# encoding=utf-8
import multiprocessing
import time


def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    print 'wait_for_event: starting'
    e.wait()  # 等待收到能执行信号，如果一直未收到将一直阻塞。e.is_set()为True时运行
    print 'wait_for_event: e.is_set()->', e.is_set()


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    print 'wait_for_event_timeout: starting'
    e.wait(t)  # 等待t秒超时,此时Event的状态仍未未设置，继续执行
    print 'wait_for_event_timeout: e.is_set()->', e.is_set()
    e.set()  # 初始内部标志为真，将e.is_set()值改成True


if __name__ == '__main__':
    e = multiprocessing.Event()
    print "begin,e.is_set()", e.is_set()  # 只有true Or false两个值,默认是False
    w1 = multiprocessing.Process(name='block', target=wait_for_event, args=(e,))
    w1.start()

    # 可将2改为5，看看执行结果
    w2 = multiprocessing.Process(name='nonblock', target=wait_for_event_timeout, args=(e, 2))
    w2.start()

    print 'main: waiting before calling Event.set()'
    time.sleep(3)
    # e.set()   #可注释此句话看效果
    # print 'main: event is set'
