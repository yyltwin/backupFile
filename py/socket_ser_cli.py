#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
      socket
          \
      bind 协议 地址 端口
          \
      listen监听客户端socket请求
          \
      accept()                                         socket
          \                                              \
    ->  阻塞等待连接请求 <<-------三次握手-----------  connect
    \     \                                              \
    \     recv          << --------------------------   send
    \     \                                              \
     ---  send             ------------------------->>   recv
          \                                               \
          close                                          close
"""







# http请求
'''
import socket
from urllib.parse import urlparse  # 解析url地址


def get_url(url):
    url = urlparse(url)
    host = url.netloc  # 主机域名
    path = url.path  # 路径
    if not path:
        path = "/"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(host, path)
    
    # 设置非阻塞， connect立即返回，但若连接未建立好，send会抛异常
    #  - > 不断询问链接是否建立好， 用while 循环不停地检查状态
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


# socket.AF_INET, sock.DGRAM
'''
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 8080))
data, addr = server.recvfrom(1024)
print(data, addr)
server.send(b"udp server")
server.close()

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(("127.0.0.1", 8080))
client.sendall(b"udp client")
data = client.recv(1024)
print(data)
client.close()

'''

# socket.AF_INET ， TCP协议
'''
import socket
server = socket.socket(socket.AF_INET)
server.bind(("0.0.0.0", 8080))
server.listen()
sock, addr = server.accept()
data = sock.recv(1024)
print(data.decode("utf-8"))
sock.close()


import socket
client = socket.socket(socket.AF_INET)
client.connect(("127.0.0.1", 8080))
client.send("yyltwin".encode())
client.close()
'''

# 多线程
'''
def handle_socket(sock, addr):
    while 1:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        sock.close()
        break

import socket
server = socket.socket(socket.AF_INET)
server.bind(("0.0.0.0", 8080))
server.listen()

while 1:
    sock, addr = server.accept()
    import threading
    client_thread = threading.Thread(target=handle_socket, args=(sock, addr))
    client_thread.start()

'''

