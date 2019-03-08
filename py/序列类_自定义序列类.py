#!/usr/bin/env python
# -*- coding:utf-8 -*-
from _collections_abc import Sequence
from _collections_abc import __all__
from _collections_abc import *
import numbers
  #  numbers 包列举出Python 中基本的数据类型

#  a += [4,5,6] ， 内部调用 __iadd__ 方法
class add:

    def __iadd__(self, other):
        print(" in += operation ")
        print("arg orther ", other)
        return self

a = add()
a += "fff"
print(a)

# slice_object
# 支持切片操作的类
#
class Group(Sequence):

    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __getitem__(self, item):
        if isinstance(item, slice):
            return Group(self.group_name, self.company_name, self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return Group(self.group_name, self.company_name, [self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __contains__(self, item):  # if .. in ... 语法所对应的方法
        if item in self.staffs:
            return True
        return False

    def __iter__(self):
        return iter(self.staffs)

    def __reversed__(self):  # reversed 函数调用的方法
        self.staffs.reverse()

a = Group("user", "company_name", ["wp1", "wp2"])

for i in a:
    print(i)

reversed(a)
print(a.staffs)