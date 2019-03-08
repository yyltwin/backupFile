#!/usr/bin/env python
# -*- coding:utf-8 -*-

# __getattr__  查找不到属性时 调用
# __getattribute__ 只要访问了属性就进入

#!/usr/bin/env python
# -*- coding:utf-8 -*-

class User:

    def __init__(self, name, age):

        self.name = name
        self._age = age

    def __getattr__(self, item):  # 查找不到属性时进入
        print("not find attr", item, type(item))

    def __getattribute__(self, item):  # 只要访问了属性就进入
        print("attrr")
        return int


user = User("wp", 18)
print(user.s())