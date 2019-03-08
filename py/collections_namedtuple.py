#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import namedtuple

User = namedtuple("User", ["name", "age", "height", "edu"])
# 创建namedtuple 1
user = User(name="wp", age=21, height=176, edu="master")
# 创建2
data = ("wp", 21, 176, "master")
user = User(*data)
# 创建3
data = {
    "name":"wp",
    "age": 21,
    "height": 176
}
user = User(**data, edu="master")

# _make方法传入一个iterable对象 初始化
data = ("wp", 21, 176, "master")
user = User._make(data)


# _asdict, 将namedtuple转化成 orderedDict 对象
user_info_dict = user._asdict()

print(user.age, user.name, user.height)

# namedtuple 是 tuple 的子类, 省空间, 效率高

# namedtuple可以使用拆包
name, age, height = user

