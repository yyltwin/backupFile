#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Semaphore 用于控制进入数量的锁

# 文件读写一般只能是一个线程写，读可以有多个

# 用于在多线程中控制并发的数量

# 内部使用condition

import time

read_num = [1,2,3,4,5,6,7,8,9,10]


def read(sem):
    global read_num
    sem.acquire()
    time.sleep(1)
    if read_num:
        print("read func reading num " + str(read_num.pop()))
    sem.release()


if __name__ == '__main__':
    import threading

    sem = threading.Semaphore(3)

    for i in range(20):
        r1 = threading.Thread(target=read, args=(sem,))
        r1.start()
