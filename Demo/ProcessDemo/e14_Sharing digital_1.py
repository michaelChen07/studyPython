#encoding=utf-8
from multiprocessing import Process

# 未使用共享变量
def f(n, a):
    n = 3.1415927
    print n
    for i in range(len(a)):
        a[i] = -a[i]
    print a
if __name__ == '__main__':
    num = 0 #
    arr = range(10)
    p = Process(target = f, args = (num, arr))
    p.start()
    p.join()
    print num
    print arr[:]


# 使用共享变量
from multiprocessing import Process, Value, Array

def f2(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0) # 创建一个进程间共享的数字类型，默认值为0
    arr = Array('i', range(10)) # 创建一个进程间共享的数组类型，初始值为range[10]
    p = Process(target = f2, args = (num, arr))
    p.start()
    p.join()

    print num.value # 获取共享变量num的值
    print arr[:]


# 统计进程的访问次数和
def f3(n):
    n.value += 1

if __name__ == '__main__':
    num = Value('d', 0.0) # 创建一个进程间共享的数字类型，默认值为0
    for i in range(5):
        p = Process(target = f3, args = (num, ))
        p.start()
        p.join()
    print num.value

