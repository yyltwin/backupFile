#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import defaultdict


# __missing__ 方法 ， 在dict没有此键的时候调用
# defaultdict 使用C语言实现, 继承dict
# 传入可调用对象， 如int() 为 0， list() 为空数组

default_dict = defaultdict(int)


nums = [1,2,3,4,5,5,4,3]
for i in nums:
    default_dict[i] += 1


# 定义函数返回所需要的结构
def gen_default():
    return {
        "name":"",
        "age":0
    }
user_info_dict = defaultdict(gen_default)

print(default_dict)