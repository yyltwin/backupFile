#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 事件循环 + 回调 （驱动生成器）+ epoll（Io多路复用）
#

import asyncio
import time
# 同步阻塞time.sleep()不能使用在协程中,无法达到多并发效果
from functools import partial

async def read(nums):
    print("start read func....", nums)
    await asyncio.sleep(2)
    print("end read func")


def callback(par_need, future):
    print("send email to ..")
    print(par_need)


if __name__ == '__main__':
    # 0, callback
    # s = time.time()
    # loop = asyncio.get_event_loop()
    # task = loop.create_task(read(2))
    # task.add_done_callback(partial(callback, "args_ssss"))
    # loop.run_until_complete(task)
    # print(time.time() - s)

    # gather 和 wait， gather 更加high-level, 可以对task进行分组

    task1 = [read(i) for i in range(10)]
    task2 = [read(i) for i in range(10)]

    group1 = asyncio.gather(*task1)
    group2 = asyncio.gather(*task2)

    # group1.cancel()  # 取消任务

    # 1
    s = time.time()
    loop = asyncio.get_event_loop()
    # tasks = [read(i) for i in range(10)]


    loop.run_until_complete(asyncio.gather(group1, group2))  # gather 加 *,
    # loop.run_until_complete(asyncio.gather(*task1, *task2))  # gather 加 *,

    print(time.time() - s)
    #
    # wait
    # s = time.time()
    # loop = asyncio.get_event_loop()
    # tasks = [read(i) for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))  # wait,
    # print(time.time() - s)
    pass
    # 2
    # s = time.time()
    # loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(read(2))
    # loop.run_until_complete(get_future)
    # print(time.time() - s)
    pass

    # 3
    # s = time.time()
    # loop = asyncio.get_event_loop()
    # task = loop.create_task(read(2))
    # print(type(task))
    # loop.run_until_complete(task)
    # print(time.time() - s)