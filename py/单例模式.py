#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 1，python 模块是单例模式

class Singleton:
    def fun(self):
        pass
singleton = Singleton()
# ----
# import singleleton


#2，装饰器
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton

@Singleton
class Cls:
    def __init__(self, x, y):
        self.x = x

a1 = Cls(1,2)
a2 = Cls(3,4)



# __new__
class Singleton:

    _instance = None

    def __new__(cls, *args, **kwargs):

        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

a = Singleton()
b = Singleton()



# type 创建类时, 执行type的 __init__ 方法，
#  类名() 执行type 的 __call__ 方法
# 3.元类
import threading
class _type(type):

    # 防止有io操作时，线程间的数据安全
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        
        if not hasattr(cls, "_instance"):
            with _type._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(_type, cls).__call__(*args, **kwargs)
        return cls._instance


class Cls(metaclass=_type):

    pass

a = Cls()
b = Cls()
print(id(a), id(b))