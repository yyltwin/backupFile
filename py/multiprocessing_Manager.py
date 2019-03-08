#!/usr/bin/env python
# -*- coding:utf-8 -*-

# manager 有些常见的数据类型实现 进程间同步

from multiprocessing import Manager, Process

def add(p_dict, key, value):
    p_dict[key] = value

def add_list(p_list, key, value):
    p_list.append(key)
    p_list.append(value)

if __name__ == '__main__':

    # 数据共享时要注意数据同步

    progress_dict = Manager().dict()
    progress_list = Manager().list()

    pro1 = Process(target=add_list, args=(progress_list, "yyltwin1", 11))
    pro2 = Process(target=add_list, args=(progress_list, "yyltwin2", 22))

    pro1.start()
    pro2.start()

    pro1.join()
    pro2.join()

    print(progress_dict)
    print(progress_list)