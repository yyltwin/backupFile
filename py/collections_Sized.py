#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Sized

# 类中实现了 __len__ 方法 ， isinstance 返回 true

class cls(Sized):

    def __init__(self):
        self.s = "string"

    def __len__(self):
        return len(self.s)


c = cls()
from collections import Counter, Mapping

print(isinstance(c, Sized))

