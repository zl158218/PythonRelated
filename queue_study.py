# -*- coding: utf-8 -*-
# 多线程， 队列
import time
import threading
import queue

class Worker(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.start()    #执行run()

    def run(self):
        #循环，保证接着跑下一个任务
        while True:
            # 队列为空则退出线程
            if self.queue.empty():
                break
            # 获取一个队列数据
            foo = self.queue.get()
            # 延时 1S 模拟你要做的事情
            time.sleep(1)
            # 打印
            print(self.getName() + " process " + str(foo))
            # 任务完成
            self.queue.task_done()


# 队列
queue = queue.Queue()
# 加入100个任务队列
for i in range(50):
    queue.put(i)
    
# 开10个线程
for i in range(10):
    threadName = 'Thread' + str(i)
    Worker(threadName, queue)
# 所有线程执行完毕后关闭
queue.join()
