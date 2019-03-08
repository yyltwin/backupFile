#!/usr/bin/env python
# -*- coding:utf-8 -*-


# py3.3新加入的语法


from itertools import chain  # 将多个可迭代对象连起来做for循环

lis = [1,2,3]
dic = {
    "yyltwin":1,
    "yyltwin2":2
}

# for i in chain(lis, dic, range(5)):
#     print(i)

def my_chain(*args, **kwargs):
    for i in args:
        yield from i

'''
def g1(gen):
    yield from gen
    
def main():
    g = g1()
    g.send(None)
    
1, main -> 调用方
2, g1 -> 委托生成器
3 gen-> 子生成器
    
yield from -> 在调用方和子生成器间建立通道
'''