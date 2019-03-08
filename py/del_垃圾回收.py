#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Cls:

    def __del__(self):
        print("in func __del__")


a = Cls()
del a
print(a)