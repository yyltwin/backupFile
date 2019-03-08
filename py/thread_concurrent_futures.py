#!/usr/bin/env python
# -*- coding:utf-8 -*-

# concurrent.futures  从Py3.2引入
# futures 包用来线程池和进程池编程

# 主线程可以获取某个线程的状态， 以及返回值

# 主线程立刻知道线程完成
# futures 可以让多线程 和 多进程 接口一致

# 学习 concurrent.futures 设计理念 -> 协程的设计理念
from concurrent.futures import Future
# 未来会完成, 未来对象， task的返回容器
# ThreadPoolExecutor -> Future ->  coroutine
# \
# Lock ->
# 生成Future ->
# 放到_WorkItem执行 ->
# 将_WorkItem放到_work_queue (任务队列)(Queue队列) ->
# _adjust_thread_count 调整线程数量 -> 判断线程池启动线程数， 若小于max_ workers,则启动线程执行_worker函数传入_work_queue 多个_worker读取同一个_work_queue ->
# 运行线程后将返回值设置到Future 对象里 （future.set_result)
# 将启动的线程加入到 _threads (set 集合)
#  return Future

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def read(sec):
    time.sleep(sec)
    print("read fun sleep" + str(sec) + "seconds.")
    return sec


if __name__ == '__main__':

    '''
    可以使用with上下文
    '''
    from concurrent.futures import as_completed
    with ThreadPoolExecutor(3) as executor:
        seconds = [3, 1, 2]
        all_exe = [executor.submit(read, *(i,)) for i in seconds]
        for future in as_completed(all_exe):
            re = future.result()
            print("reutrn msg :", re)






    # # submit 返回 Future 对象
    #
    # # sumbit 是非阻塞， 立即返回
    #
    # # cancel 取消操作， 成功返回True, 已开始的线程不能cancel , cancel 成功的线程掉用result 会异常
    #
    # # rusult  ， 阻塞， 得到执行结果
    #
    # executor = ThreadPoolExecutor(max_workers=1)
    #
    # exe1 = executor.submit(read, *(3,))
    #
    # exe2 = executor.submit(read, *(2,))
    #
    # print("cancel func:", exe2.cancel())
    #
    # print("exe1 .done func:", exe1.done())
    # time.sleep(4)
    # print("exe1 .done func:", exe1.done())  # 判断任务是否执行成功
    #
    # print("result func:", exe1.result())  # 阻塞
    #
    pass



if __name__ == '__main__':
    # 要获取已经成功的 exe 的返回

    from concurrent.futures import as_completed

    # as_completed 使用生成器实现 ， 将已经完成的 exe 返回

    # submit 返回 Future 对象

    # executor = ThreadPoolExecutor(max_workers=2)
    #
    # seconds = [3, 1, 2]
    #
    #
    # all_exe = [executor.submit(read, *(i,)) for i in seconds]
    #

    # as_completed 哪个先完成先返回值

    # wait() 阻塞等待线程完成

    # return_when 参数指定 何时返回 ， 默认是 ALL_COMPLETED
    '''
    FIRST_COMPLETED = 'FIRST_COMPLETED'
    FIRST_EXCEPTION = 'FIRST_EXCEPTION'
    ALL_COMPLETED = 'ALL_COMPLETED'
    '''

    # from concurrent.futures import wait, FIRST_COMPLETED
    #
    # wait(all_exe, return_when='ALL_COMPLETED')
    # print(" all done")  # 完成后等待

    # for future in as_completed(all_exe):
    #
    #     re = future.result()
    #     print("reutrn msg :", re)



    pass


    # 通过 executor 获取已经完成的 exe

    # map 函数的返回值顺序 与 传入参数的顺序一致

    # for re in executor.map(read, seconds):
    #
    #     print("reutrn msg : ", re)

