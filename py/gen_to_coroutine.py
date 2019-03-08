#!/usr/bin/env python
# -*- coding:utf-8 -*-
import inspect

# 使用 inspect.getgeneratorstate(gen) 获取生成器状态

# 生成器是可以暂停的函数



def gen_func():
    yield 1
    return "bobby"


if __name__ == '__main__':
    gen = gen_func()

    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
