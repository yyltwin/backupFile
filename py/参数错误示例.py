#!/usr/bin/env python
# -*- coding:utf-8 -*-


def add(a, b):

    a += b
    return a

if __name__ == '__main__':

    a = 1
    b = 2

    a = [1,2]  # 参数会随函数里面的操作改变值
    b = [3,4]

    c = add(a, b)

    print(c)
    print(a, b)

    a = (1,2)
    b = (3,4)

    c = add(a, b)

    print(c)
    print(a, b)