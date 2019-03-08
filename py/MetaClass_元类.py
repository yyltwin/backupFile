#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 类的实例化过程

# 首先寻找自己或基类 metaclass ， 通过metaclass创建类
# class a: pass,
# type 去创建 类对象 ，
import numbers

class Field: pass

class IntField(Field):

    def __init__(self, db_column, min_value=None, max_value=None):

        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")

            if not isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("man_value must be positive int")

            if min_value is not None and max_value is not None:
                if min_value > max_value:
                    raise ValueError("min_value must smaller than max_value")

        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise TypeError("int value needed")
        # if value < 0:
        #     raise ValueError("positive int needed")

        if value > self.max_value or value < self.min_value:
            raise ValueError("value must between min_value and max_value")
        self._value = value


class CharField(Field):
    def __init__(self, db_column, max_length=None):
        if max_length is None:
            raise ValueError("you must specify max_length for charfield")
        self._value = None
        self.max_length = max_length
        self.db_column = db_column

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("string value needed")
        if len(value) > self.max_length:
            raise ValueError(" value len excess of max length")
        self._value = value

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        if name == "BaseModel":
            return super(ModelMetaClass, cls).__new__(cls, name, bases, attrs, *args, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value

        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super(ModelMetaClass, cls).__new__(cls, name, bases, attrs, *args, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            return super(BaseModel, self).__init__()
        
    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            if isinstance(value, str):
                value = "'{}'".format(value)
            values.append(str(value))
        sql = "insert {db_table}({fields}) value({values})".format(db_table=self._meta["db_table"],
                                                                   fields=",".join(fields),
                                                                   values=",".join(values))
        pass


class User(BaseModel):

    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", min_value=0, max_value=100)

    class Meta:
        db_table = "user"


if __name__ == '__main__':
    user = User(name="wp", age=28)
    # user.name = "wp"
    user.age = 28
    user.save()