#!/usr/bin/env python
# -*- coding:utf-8 -*-

# condition 用于复杂的线程间同步， 是线程中最复杂的同步锁

# Condition有两层锁，一把底层锁会在线程使用了wait方法的时候释放，
# 上面的锁会在每次调用wait的时候分配一把并放入到cond的waters队列中等待notify方法的唤醒



import threading


read_line = [1,2,3,4,5,6]


class read1(threading.Thread):

    def __init__(self, name, cond):
        self.cond = cond
        super().__init__(name=name)

    def run(self):
        global read_line
        self.cond.acquire()
        while 1:
            if len(read_line):
                self.cond.wait()
                print("read1, read_line_num", read_line.pop())
                self.cond.notify()
            else:
                break
        self.cond.release()


class read2(threading.Thread):

    def __init__(self, name, cond):
        self.cond = cond
        super().__init__(name=name)

    def run(self):
        global read_line
        with self.cond:
            while 1:
                if len(read_line):
                    print("read2, read_line_num", read_line.pop())
                    self.cond.notify()
                    self.cond.wait()
                else:
                    break


if __name__ == '__main__':
    # 1,线程的启动顺序很重要
    # 2，with 可以代替 acquire和release的组合
    # 3，必须在cond.acquire之后才能调用wait和notify, 否则报错
    #  notify 方法申请并把锁放入 waters 队列， wait 拿到解锁并继续执行
    #  notify_all 方法释放waters 队列里的所有锁, 包括主线程也会启动

    cond = threading.Condition()
    r1 = read1("read1", cond)
    r2 = read2("read2", cond)

    r1.start()
    r2.start()

    r1.join()
    r2.join()

