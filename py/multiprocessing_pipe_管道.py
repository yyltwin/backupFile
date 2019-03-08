#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process
from queue import Queue
# 多进程不能使用多线程 Queue
# 进程池不能用 Queue 通信
from multiprocessing import Pipe, Pool
import time


# pipe 的性能高于 Queue,


def producer(pipe):

    pipe.send("yyltwin")

def consumer(pipe):

    recv = pipe.recv()
    print("in func consumer", recv)


if __name__ == '__main__':
    receive_pipe, send_pipe = Pipe()

    # pipe 只能只用于两个进程间通信

    pro1 = Process(target=producer, args=(send_pipe,))
    pro2 = Process(target=consumer, args=(receive_pipe,))

    pro1.start()
    pro2.start()

    pro1.join()
    pro2.join()
    pass


