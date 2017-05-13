#encoding=utf-8
import multiprocessing as mp
import time
def consumer(cond):
    with cond:
        print("consumer before wait")
        cond.wait() # 等待消费，释放锁，等待cond.notify_all()通知。
        print("consumer after wait")

def producer(cond):
    with cond:
        print("producer before notifyAll")
        cond.notify_all() # 通知消费者可以消费了
        print("producer after notifyAll")

if __name__ == '__main__':
    condition = mp.Condition()  #条件对象，默认内部有个锁

    p1 = mp.Process(name = "p1", target = consumer, args=(condition,))
    p2 = mp.Process(name = "p2", target = consumer, args=(condition,))
    p3 = mp.Process(name = "p3", target = producer, args=(condition,))

    p1.start()
    time.sleep(2)
    p2.start()
    time.sleep(2)
    p3.start()
