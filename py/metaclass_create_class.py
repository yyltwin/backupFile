#!/usr/bin/env python
# -*- coding:utf-8 -*-


def create_class(name):

    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User

    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company


def say(self):
    return self.name






class baseclass:
    def answer(self):
        return "i am baseclass"


class metaclass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)



class user(metaclass= metaclass):


# 什么是元类 ， 元类是创建类的类， 对象<-class(对象)<-type           ,type即为元类

if __name__ == '__main__':
    cls = type("user", (baseclass,), {"name":"bob", "say":say})
    cls = cls()
    print(cls.answer())