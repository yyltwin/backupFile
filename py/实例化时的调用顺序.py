#!/usr/bin/env python
# -*- coding:utf-8 -*-



# 实例化时不会调用__call__
class Cls:

    def __new__(cls, *args, **kwargs):
        print("in __new__")
        return super(Cls, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print("__init__")
        self.x = 1

    def __call__(self, *args, **kwargs):
        print("__call__")
        return self

a = Cls()
a() # 调用__call__