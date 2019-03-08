#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process
from queue import Queue
# 多进程不能使用多线程 Queue

from multiprocessing import Queue
import time

def producer(queue):

    queue.put("a")
    time.sleep(2)

def consumer(queue):

    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == '__main__':

    # ！进程间数据隔离
    ''''''
    # queue = Queue(10)
    # task = [producer, consumer]
    # #
    # s = time.time()
    # #
    # for j, i in enumerate(task):
    #     pro = Process(target=i, args=(queue,))
    #     pro.start()
    #     task[j] = pro
    #
    # for i in task:
    #     i.join()
    #
    # print("end.", time.time() - s)
    ''''''
    # produ = Process(target=producer, args=(queue,))
    # consu = Process(target=consumer, args=(queue,))
    #
    # produ.start()
    # consu.start()
    #
    # produ.join()
    # consu.join()
    #
    # print("end", time.time() - s )
    pass

    from multiprocessing import Pool, Manager

    # 多进程进程Queue 不能用于直接进程池， 要用Manager().Queue(), 先实例化
    queue = Manager().Queue(10)
    pool = Pool(2)

    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))

    pool.close()
    pool.join()

    pass
