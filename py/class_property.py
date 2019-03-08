#!/usr/bin/env python
# -*- coding:utf-8 -*-

class User:

    def __init__(self, name, age):

        self.name = name
        self._age = age


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        self._age = value



user = User("wp", 18)
user.age = 1
print(user.age)