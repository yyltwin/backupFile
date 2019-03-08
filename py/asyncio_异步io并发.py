#!/usr/bin/env python
# -*- coding:utf-8 -*-

# py3.4之后引入
# 转变同步io编程思维

# 事件循环 + 回调 （驱动生成器）+ epoll（Io多路复用）

# 用于解决异步io编程的一套解决方案
# 基于此的框架, tornado gevent twisted(scrapy, django channels)

# tornado(实现了web服务器) -> 可以直接部署 -> nginx + tornado
# django + flask -> 阻塞io -> 本身不提供web服务器， 不完成socket编码 ->(uwsig, gunicorn + nginx)

#  - > 包含各种特定系统实现的模块化事件循环
#  -> 传输和协议抽象
#  -> 对TCP,udp,ssl子进程，延时调用以及其他的具体指示
#  -> 模仿futures模块但适用于时间循环的Future类
#  -> 基于yield from 的协议和任务， 用同步方式编写异步代码
#  -> 必须使用一个将产生阻塞Io的调用时， 有接口可以八事件转移到线程池
#  -> 模仿threading模块中的同步原语，可以用在单线程内的协程之间