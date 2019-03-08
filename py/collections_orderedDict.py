#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import OrderedDict

user_dict = OrderedDict()


# py3.x dict 默认有序，


user_dict["a"] = "wp1"
user_dict["b"] = "wp2"
user_dict["c"] = "wp3"

# move_to_end  把键值对移到最后
user_dict.move_to_end("b")