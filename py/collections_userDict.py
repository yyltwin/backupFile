#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import UserDict

# 用于自定义类继承 由C实现的内置类如dict,

class MyDict(UserDict):  # 继承dict可能达不到预期效果

    def __setitem__(self, key, value):
        super(MyDict, self).__setitem__(key, value * 2)



d = MyDict(one=1)
print(d)

