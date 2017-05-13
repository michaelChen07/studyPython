# encoding=utf-8
from multiprocessing import Process, Manager, Value
from ctypes import c_char_p

def greet(shareStr):
    shareStr.value = shareStr.value + ", World!"

if __name__ == '__main__':
    manager = Manager()
    shareStr = manager.Value(c_char_p, "Hello")
    process = [Process(target = greet, args = (shareStr,)) for i in range(5)]
    for p in process: p.start()
    for p in process: p.join()

    # 等价于
    # for i in range(5):
    # process = Process(target = greet, args = (shareStr,))
    #process.start()
    #process.join()
    print shareStr.value
