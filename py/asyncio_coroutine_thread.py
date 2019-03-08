#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 代码中必要阻塞操作可以放到线程池中运行
# threadPoolExecutor + asyncio

import asyncio

import socket
from urllib.parse import urlparse  # 解析url地址



def get_url(url):
    url = urlparse(url)
    host = url.netloc  # 主机域名
    path = url.path  # 路径
    if not path:
        path = "/"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置非阻塞， connect立即返回，但若连接未建立好，send会抛异常
    #  - > 不断询问链接是否建立好， 用while 循环不停地检查状态
    #  - > 若之后的命令不依赖于连接的建立，可以利用cpu执行其他命令

    # client.setblocking(False)

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


if __name__ == '__main__':
    import time
    s = time.time()

    from concurrent.futures import ThreadPoolExecutor
    executor = ThreadPoolExecutor(3)
    loop = asyncio.get_event_loop()

    tasks = []

    for i in range(20):
        url = "http://www.baidu.com/{}/".format(i)
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)


    loop.run_until_complete(asyncio.wait(tasks))
    print("last time: ", time.time() -s)
