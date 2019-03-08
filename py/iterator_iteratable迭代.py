#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections.abc import Iterator, Iterable
from _collections_abc import Iterable, Iterator


class Company:
    def __init__(self, emp_list):
        self.emp_lis = emp_list

    def __iter__(self):
        return MyIterator(self.emp_lis)

    def __getitem__(self, item):
        return self.emp_lis[item]


class MyIterator(Iterator):
    def __init__(self, emp_list):
        self.emp_lis = emp_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.emp_lis[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return result


if __name__ == '__main__':
    company = Company(["bob", "juice", "julia"])
    print(len(company))
    # it = iter(company)
    # while 1:
    #     try:
    #         print(next(it))
    #     except StopIteration:
    #         break


    # iter(obj) 会首先寻找 __iter__, 然后是 __getitem__ (从零开始遍历)
#     
