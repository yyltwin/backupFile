#!/usr/bin/env python
# -*- coding:utf-8 -*-


# GIL, global interpreter lock , 全局解释器锁
# 同一时刻只有一个线程在 一个 cpu上执行， 无法将多个线程运行在多个cpu上

# gil会根据执行的字节码行数以及时间片释放

# 遇到IO操作会释放

# pypy解释器是 无 gil 的






