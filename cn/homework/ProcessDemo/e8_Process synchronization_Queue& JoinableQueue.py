#encoding=utf-8
import multiprocessing
import time
class Consumer(multiprocessing.Process):
    # 派生进程
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    # 重写原进程的run方法
    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                print ('%s: Exiting' % proc_name)
                self.task_queue.task_done()
                break
            print ('%s: %s' % (proc_name, next_task))
            answer = next_task() # __call__()
            self.task_queue.task_done()
            self.result_queue.put(answer)
        return
class Task(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self):
        time.sleep(0.1) # pretend to take some time to do the work
        return '%s * %s = %s' % (self.a, self.b, self.a * self.b)
    def __str__(self):
        return '%s * %s' % (self.a, self.b)

if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    # Start consumers
    num_consumers = multiprocessing.cpu_count()
    print ('Creating %d consumers' % num_consumers)
    # 创建cup核数量数量个的子进程
    consumers = [ Consumer(tasks, results) for i in range(num_consumers) ]
    # 依次启动子进程
    for w in consumers:
        w.start()
    # Enqueue jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)
    # Wait for all of the tasks to finish
    tasks.join()

    # Start printing results
    while num_jobs:
        result = results.get()
        print 'Result: %s' %result
        num_jobs -= 1
