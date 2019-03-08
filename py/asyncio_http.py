#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio
# asyncio 没有提供http协议的接口


import socket
from urllib.parse import urlparse  # 解析url地址


async def get_url(url):
    url = urlparse(url)
    host = url.netloc  # 主机域名
    path = url.path  # 路径
    if not path:
        path = "/"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ->
    reader, writer = await asyncio.open_connection(host, 80)

    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    all_line = []
    #     async for 异步 for 语法
    async for raw_line in reader:
        data = raw_line.decode("utf8")
        all_line.append(data)
    html = "\n".join(all_line)
    return html


async def main(loop):
    tasks = []
    for i in range(20):
        url = "http://www.baidu.com/{}/".format(i)
        tasks.append(asyncio.ensure_future(get_url(url)))

    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == '__main__':
    import time
    s = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    print("last time: ", time.time() - s)

    pass
