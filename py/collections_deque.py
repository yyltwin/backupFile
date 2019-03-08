#!/usr/bin/env python
# -*- coding:utf-8 -*-


# deque , 使用c语言实现
# 可以从队列前和后操作队列

# queue.Queue 内部使用 deque 实现

from collections import deque
# -----------
     # deque 是线程安全的
# -----------

#  双端队列 deque 已经在字节码级别上达到 线程安全
from collections import deque
import time

nums = deque(maxlen=30) # 设置最大长度

def get(nums_p):
    while 1:
        try:
            n = nums_p.pop()
            if n is None:
                break
            time.sleep(0.5)
            print("get func :", n)
        except IndexError:
            pass


def put(nums_p):

    for i in range(10):
        time.sleep(0.3)
        nums_p.append(i)
    nums_p.append(None)
    print(nums_p)


if __name__ == '__main__':

    # t1 = threading.Thread(target=put, args=(nums,))
    # t1.start()
    #
    # t2 = threading.Thread(target=get, args=(nums,))
    # t2.start()
    #
    # t2.join()
    # t1.join()
    pass









# 取文件    最后   maxLen  行，
#  maxLen 固定长度时， 后入的数据会把先入的挤出去，

def tail(file, n=10):
    with open(file) as f:
        return deque(f, maxlen=10)
# print(tail("read_file"))



user_list1 = deque(["wp1", "wp2"])  # 传入字典时默认取key值存入
user_list2 = deque(["wp3", "wp4"])


user_list2.reverse() # 反转
user_list2.count("wp3")  # 统计个数

user_list2.rotate(3)  # 旋转移动元素 正数向右， 负数向左
user_list2.rotate(-3)


# extend ; extendleft 对当前元素进行修改
user_list1.extend(user_list2)
user_list1.extendleft(user_list2)

'''
from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

# Example use on a file
if __name__ == '__main__':
    with open(r'read_file') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
'''