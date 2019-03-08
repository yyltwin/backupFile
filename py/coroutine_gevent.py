#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 使用monkey;monkey.patch_all() 识别其他IO操作

from gevent import monkey;
monkey.patch_all()

import gevent
import time


def eat():
    print('eat food 1')
    time.sleep(2)
    print('eat food 2')


def play():
    print('play 1')
    time.sleep(1)
    print('play 2')


g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)
gevent.joinall([g1, g2])
print('主')
