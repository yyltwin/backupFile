#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time

# fork 新建  子进程 ， 只能用于 linux/unix
'''
pid = os.fork()
print("yyltwin")

if pid==0:
    print("子进程 {}, 父进程 {}".format(os.getpid(), os.getppid()))
else:
    print("父进程 {}", pid)
    
time.sleep(2)
'''

from concurrent.futures import ProcessPoolExecutor # 首选

import multiprocessing

import time
import os


def read(n):
    time.sleep(n)
    print("sub process, ", os.getppid())
    return n


if __name__ == '__main__':
    # progress = multiprocessing.Process(target=read, args=(2,))
    # progress.start()
    # progress.join()
    # print("end.")


    pass

    # 使用进程池
    #
    pool = multiprocessing.Pool(3)  # 不指定数量默认为CPU_count
    # # 进程数等于CPU数量性能最高
    #
    # print(multiprocessing.cpu_count())
    #
    # result = pool.apply_async(read, args=(3,))
    #
    #
    # # pool.terminate()
    # pool.close()  # join 之前必须关闭， 停止接受任务， 否则会异常
    # '''
    # assert self._state in (CLOSE, TERMINATE)
    # '''
    # pool.join()  # 等待进程池所有进程完成, 非close状态和TERMINATE状态会报错
    #
    # print(result.get())  # 返回值

    pass

    # imap , 类似ProcessingPoolExecuter 里 map 方法

    # 返回结果顺序和传入迭代顺序一样
    for result in pool.imap(read, [1,5,3]):
        print(result)

    pass

    # imap_unordered, 无序

    # 返回值按执行完成时间排序

    for result in pool.imap_unordered(read, [1,5,3]):
        print(result)

    pass