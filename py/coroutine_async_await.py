#!/usr/bin/env python
# -*- coding:utf-8 -*-

# py3.5之后引入async 和 await 关键字用于定义原生的协程,使代码易于维护阅读

from collections import Awaitable

# await关键字返回一个Awaitable对象

# async 不能使用yield

async def downloader(url):
    return "bobby"

# 无async语法
import types
@types.coroutine
def downloader1(usl):
    yield "bobby"

async def download_url(url):
    html = await downloader1(url)
    return html

if __name__ == "__main__":
    coro = download_url("http://www.imooc.com")
    # next(coro)  # 不能使用next
    coro.send(None)
    pass

# 配合事件循环使用
#     协程的调度是 事件循环 + 协程 模式
#     与回调模式区别：不需要建立类，， 函数内的代码可以直接访问
#     异常会向上冒泡抛给调用方
#     不能编写耗时操作， 遇到IO直接yield 回到事件循环继续执行下一个协程操作


