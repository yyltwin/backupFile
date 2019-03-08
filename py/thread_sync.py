#!/usr/bin/env python
# -*- coding:utf-8 -*-


num = 0
# 线程同步
# 锁，和可重入锁，** 在同一个线程，Rlock可连续进行多次acquire， 必须有相同数量的release
# 锁 会影响性能
# 会出现死锁，1，两个acquirex写到一起，
#             3，互相等待



def add(lock):
    global num
    for i in range(1000000):
        with lock:
        # num += 1
            do_something(lock, num)


def do_something(lock, num):
    with lock:
        num += 1


def desc(lock):
    global num
    for i in range(1000000):
        with lock:
            i -= 1


if __name__ == '__main__':

    from threading import Thread,Lock, RLock


    lock = RLock()

    a = Thread(target=add, args=(lock,))
    b = Thread(target=desc, args=(lock,))

    a.start()
    b.start()

    a.join()
    b.join()

    print(num)

