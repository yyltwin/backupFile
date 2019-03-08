#!/usr/bin/env python
# -*- coding:utf-8 -*-

# counter 为 dict 的子类

from collections import Counter


user = ["wp1", "wp2", "wp3", "wp1", "wp2"]

user_counter = Counter(user)


# update 方法可以添加统计的数据

user = Counter("abcdefg")
user.update("abcdefg")

# most_common 统计出现次数最多的前 n 个元素
n = 2
print(user.most_common(n)) # 返回列表

print(user)