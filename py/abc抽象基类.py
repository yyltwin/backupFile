#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 抽象基类不能实例化


from collections.abc import *

import abc

class AbsDict(metaclass=abc.ABCMeta):

    pass

class A:
    pass

AbsDict.register(dict)

print(isinstance(dict(), AbsDict))
print(issubclass(dict, AbsDict))
print(isinstance(int, type))