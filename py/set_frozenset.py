#!/usr/bin/env python
# -*- coding:utf-8 -*-

# set  无序 不重复
# frozenset 不可变集合


a = set("abc")
b = frozenset("abcdd")

# frozenset 可以作为 dict 的 key

d = {}

d[b] = "frozenset"

# a.update(b)

print(a,b,d)
