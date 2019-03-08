#!/usr/bin/env python
# -*- coding:utf-8 -*-


# loop会被放到future中
# 取消task

import asyncio

async def read(sleep_time):
    print("in read func,sleep_time:", sleep_time)
    await asyncio.sleep(sleep_time)
    print("end read func")

if __name__ == '__main__':

    tasks = [read(i) for i in range(3,10,2)]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))

    except KeyboardInterrupt:

        all_task = asyncio.Task.all_tasks()
        for task in all_task:
            print("cancel task:")
            print(task.cancel())

        loop.stop()
        loop.run_forever()

    finally:
        loop.close()

