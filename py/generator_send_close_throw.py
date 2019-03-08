#!/usr/bin/env python
# -*- coding:utf-8 -*-
# !拿到生成器对象的就可以对其进行操作

def gen_func():

    nums = yield "yield out"
    print(nums)
    yield 1
    yield 2
    return "yyltwin"


if __name__ == '__main__':
    # gen = gen_func()
    # print(next(gen))
    # print(gen.send("message1"))
    # print(next(gen))
    pass


# close

def gen_func():
    try:
        nums = yield "yield out"
    except GeneratorExit as e:  # GeneratorExit 继承自 BaseException
        raise StopIteration
        pass
    yield 1
    yield 2
    return "yyltwin"


if __name__ == '__main__':
    # gen = gen_func()
    # print(next(gen))
    # gen.close()  # 内部抛出GeneratorExit, 未处理时会抛出RuntimeError , 之后对生成器的操作会抛出StopIteration，, 函数return 也取不到
    # print(next(gen))
    pass


def gen_func():
    try:
        nums = yield "yield out"
    except Exception as e:
        pass
    yield 1
    yield 2
    return "yyltwin"


if __name__ == '__main__':
    gen = gen_func()
    print(gen.__next__())
    print(gen.throw(Exception, "error message"))
    print(next(gen))
    pass