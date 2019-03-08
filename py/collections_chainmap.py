#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 重复的键只会取第一个， 每个键


from collections import ChainMap

user1 = {"a":"wp1", "b":"wp2"}
user2 = {"b":"wp3", "e":"wp4"}

new_dict = ChainMap(user1, user2)

# # new_child 追加 新的dict
# new_dict.new_child({"f":"wp6"}) ????????

# 属性maps 以列表的形式将数据展示出来, 非拷贝， 可以修改原数据
print(new_dict.maps)

for i, j in new_dict.items():
    print(i, j)
