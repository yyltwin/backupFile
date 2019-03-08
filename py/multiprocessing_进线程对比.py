#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 进程切换调度代价高于线程

# 耗费cpu操作，计算密集型 -> 进程 > 线程

def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)


from concurrent.futures import as_completed, ThreadPoolExecutor, ProcessPoolExecutor
import time


if __name__ == '__main__':
    # 计算密集型 线程优于 线程
    # with ProcessPoolExecutor(3) as executor:
    #     seconds = [3, 1, 2]
    #     all_exe = [executor.submit(fib, *(i,)) for i in range(24, 35)]
    #
    #     start_time = time.time()
    #
    #     for future in as_completed(all_exe):
    #         re = future.result()
    #         print("reutrn msg :", re)
    #
    #     print("last time is ", time.time() - start_time)

    pass




def random_sleep(n):
    time.sleep(n)
    return n



if __name__ == '__main__':
    # IO密集型， 线程优于进程
    with ThreadPoolExecutor(3) as executor:
        seconds = [3, 1, 2]
        all_exe = [executor.submit(random_sleep, *(i,)) for i in range(3)]

        start_time = time.time()

        for future in as_completed(all_exe):
            re = future.result()
            print("reutrn msg :", re)

        print("last time is ", time.time() - start_time)

    pass