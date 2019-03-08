#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 作业： 使用此模式实现高并发多人聊天群

# 此模式缺点

# 可读性差
# 共享状态管理困难
# 异常处理困难

# 解决 ： 协程， 代码容易理解 ，性能高

import socket
from urllib.parse import urlparse  # 解析url地址
import select
# selectors 是 select 封装,
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# 不使用函数的方式完成
# tornado , gevent, Twisted, 基于此模式
# select + 回调 + 时间循环
# \
# 高并发
# 单线程 - 省去了线程切换的开销 - 协程的关键

selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False


class Fetcher:
    def get_utl(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc  # 主机域名
        self.path = url.path  # 路径
        self.data = b""
        if not self.path:
            self.path = "/"
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass

        # 注册

        '''
        fileobj -> socket.fileno() -> socket 的文件描述符
        events -> 
        data -> callback function
        '''
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

    def connected(self, key):
        selector.unregister(key.fd)  # key.fd 是 client.fileno() 的返回值
        print("key.fd", key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(
            self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

        print("client.fileno", self.client.fileno())

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            print(d)
            self.data += d
        else:
            selector.unregister(key.fd)
            self.data = self.data.decode("utf8")  # 返回 请求头 和 内容
            headers, html_data = self.data.split("\r\n\r\n")
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True


def loop():  # 事件循环，不停请求socket状态并调用对应的call_back函数
#     select 本身不支持register模式， 只能够传递进句柄
#       socket 状态变化后的回调是由程序员完成而非操作系统， 操作系统完成的模式是aio
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.datar
            call_back(key)
    pass


if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_utl("http://www.baidu.com")

    loop()

'''
---------------------------------------------------------------------
'''

'''
def get_url(url):
    url = urlparse(url)
    host = url.netloc  # 主机域名
    path = url.path  # 路径
    if not path:
        path = "/"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(host, path)
    
    # 设置非阻塞， connect立即返回，但若连接未建立好，send会抛异常
    #  - > 不断询问链接是否建立好， 用while 循环不停地检查状态, 
    #  - > 若之后的命令不依赖于连接的建立，可以利用cpu执行其他命令
    
    client.setblocking(False)
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while 1:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")  # 返回 请求头 和 内容

    headers, html_data = data.split("\r\n\r\n")

    print(html_data)
    client.close()


get_url("http://www.baidu.com")

'''