#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio


def callback(sleep_times):

    print("sleep time", sleep_times)

def stop(loop):  # 用于停止forever
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # call_soon_threadsafe 线程安全


    now = loop.time()
    loop.call_at(now + 2, callback, 11)  # 相对于loop.time的时间

    loop.call_later(2, callback, 2)  # delay s 秒后执行, 与传入顺序无关, 根据delay 排列先后顺序
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)

    loop.call_soon(callback, 2)  # 立即执行
    # loop.call_soon_threadsafe(callback, 2)

    # loop.call_soon(stop, loop)
    loop.run_forever()

    # loop.run_until_complete()  # 用于协程
