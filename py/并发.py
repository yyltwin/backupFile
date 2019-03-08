# #!/usr/bin/env python
# # -*- coding:utf-8 -*-

# ?既然同一时刻只能有一个cpu运行程序，那怎么保证io操作的完成？

# 并发：（concurrent）一段时间内，有几个程序在同一个cpu运行，但任意时刻只有一个程序在CPU上运行
# 并行：(parallel)任意时刻，有多个程序运行在多个cpu上
# 同步：（synchronous）代码调用IO操作时， 必须等待IO操作完成才能返回
# 异步：(asynchronous) 代码调用IO操作时， 不必等待IO操作完成就能返回

# 同步和异步是消息通信的机制

# 阻塞：（block) 调用函数时候当前线程被挂起
# 非阻塞：(unblock) 调用函数时当前线程不会被挂起，立即返回

# 阻塞非阻塞是函数调用的机制

'''
unix IO模型

阻塞式io
非阻塞式io
io 多路复用(技术成熟稳定,用的最多) -> select poll epoll (本质上是同步io,要在读写事件就绪后自己负责进行读写，,阻塞方法，与while区别于可以同时监听多个IO请求)-> 让操作系统返回完成的Io操作
信号驱动式 io
异步io （读写事件就绪后，无需自己进行读写，异步io实现会负责把数据拷贝到用户空间）

'''
# select : 最早的Io多路复用技术， 跨平台，几乎支持所有操作系统， 单个进程能够监视的文件描述符有限
# poll, 查询效率高select, 没有最大限制
# epoll, linux支持， linux2.6内核提出， 查询使用 红黑树 ， nginx用的epoll

# 1，epoll并不代表一定比select好
# 并发高，连接不活跃， epoll比select 好
# 并发不高， 链接活跃, select 好
