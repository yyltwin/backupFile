#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 对于IO操作来说，多线程和多进程性能差别不大

import time
import threading

def get():
    print("in get func")
    time.sleep(2)
    print("end get func")

def put():
    print("in put funcc")
    time.sleep(2)
    print("end put func")


if __name__ == '__main__':
    thread1 = threading.Thread(target=get, args=())
    thread2 = threading.Thread(target=put, args=())

    thread1.setDaemon(True)  # 使线程随主线程退出， 守护线程
    thread2.setDaemon(True)

    thread1.start()
    thread2.start()

    thread1.join()  # 阻塞等待线程结束
    thread2.join()


class MyThread(threading.Thread):

    def __init__(self, name):
        super(MyThread, self).__init__(name=name)

    def run(self):
        print("in run func")
        time.sleep(3)
        print("end run func")


if __name__ == '__main__':
    thread1 = MyThread("yyltwin")
    thread1.start()

