#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 函数中存在 yield 关键字， 生成器函数， 调用返回 generator 对象

# 生成器对象 generator 在python 编译字节码的时候就产生了
# 惰性求值

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

# print(fib(10))

def fib2(index):
    re_list = []
    n,a,b = 0,0,1
    while n < index:
        re_list.append(b)
        a,b = b, a+b
        n+=1

    return re_list
# print(fib2(10))

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1

# f = gen_fib(10)
# [print(i) for i in f]



global frame

import inspect

def A():
    print("in A")
    B()

def B():

    global frame
    frame = inspect.currentframe()  # 获取当前函数的栈帧
    pass

A()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)
# A 中调用 B
# B 栈帧中的 f_back 指向其调用者的栈帧(A)
# frame.f_code.co_name 为调用者的名字 (函数名)

# import dis
#
# print(dis.dis(A))


# python.exe 会用 PyEval_EvalFrameEx 去执行 A 函数， 首先会创建栈帧

# A 函数执行 B 函数， 会创建一个栈帧

# 所有的栈帧都是分配在堆内存上， 栈帧可以独立于调用者存在


def gen_func():
    yield 1
    name = "wp"
    yield 2
    age = 20
    yield 3
    return "imooc"  # 返回值为 StopIteration的value


gen = gen_func()
import dis
print(dis.dis(gen))

# for i in gen:
#     print(gen.gi_frame.f_lasti, gen.gi_frame.f_locals)
print(gen.gi_frame.f_lasti, gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti, gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti, gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti, gen.gi_frame.f_locals)
try:
    next(gen)
except StopIteration as e:
    print(e.value)  # 返回值

# 生成器对象 对 frame 对象进行封装

# PyGenObject {gi_frame, gi_code}
#               /          \
#             /             \
#           /                \
#   PyFrameObject       PyCodeObject
# {f_lasti, f_locals}   {bytecode -> 字节码}

# f_lasti -> 生成器执行位置, 为 -1 时生成器没有执行， 位置可以用dis.dis(gen)查看
# f_local -> 该位置的变量, 未执行为空字典


from collections import UserList


def read_line(f, newline, buf_size=4096):

    buf = ""
    while 1:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(buf_size)

        if not chunk:
            # 读到尾部退出
            yield buf
            break
        buf += chunk



