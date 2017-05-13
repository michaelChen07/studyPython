#encoding=utf-8

import multiprocessing
import time


def worker(s, i):
    s.acquire()
    print(multiprocessing.current_process().name + " acquire")
    time.sleep(i)
    print(multiprocessing.current_process().name + " release")
    s.release()
if __name__ == "__main__":
  # 设置限制最多3个进程同时访问共享资源
    s = multiprocessing.Semaphore(3)
    for i in range(5):
        p = multiprocessing.Process(target = worker, args = (s, i * 2))
        p.start()