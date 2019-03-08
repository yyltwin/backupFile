#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numbers

class IntField:
    # 数据描述符 DataDescriptor

    value = None

    def __get__(self, instance, owner):
        if not self.value:
            return 100
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, numbers.Integral):
            raise TypeError("int value need")
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    # 数据描述符 DataDescriptor

    value = None

    def __get__(self, instance, owner):
        if not self.value:
            return 99
        return self.value


class A:
    # age = 66

    def __getattr__(self, item):
        return 66


class User(A):

    # age = IntField()
    # age = NonDataIntField()
    pass


if __name__ == '__main__':
    # print(User.__dict__)
    user = User()
    print(user.age)

    # user.age 访问属性时， getattr(user, "age")，
    # 首先调用 __getattribute__ ，
    # 如果定义了 __getattr__ ,
    # __getattribute__ 抛出AttributeError时会调用 __getattr__

    """
     属性描述符 __get__ 发生在 __getattribute__ 内部.
     user.age 查找顺序:
        (1)若age是属性描述符 dataDescriptor, 
                从 User 和 基类的 __dict__ 查找, 调用dataDescriptor 的 __get__ 方法
                
        (2)从 obj 的 __dict__ 中查找, 若不存在:
        
        (3)User 或 基类 的 __dic__ 中查找, 
            （3.1） 若 age 是 non-data descriptor , 调用 __get__ 方法 
            （3.2） 否则， 返回 __dict__["age"]
            
        (4) User 有 __getattr__ 方法, 则调用, 
        
        (5) 否则， 抛出 AttributeError
       
    """