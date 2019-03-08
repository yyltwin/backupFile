#!/usr/bin/env python
# -*- coding:utf-8 -*-

# event 锁

from threading import Event, Thread
import time

class Thr(Thread):

    def __init__(self, event):
        super(Thr, self).__init__()
        self.event = event

    def run(self):

        if not self.event.isSet():
            print(" thread is ready")
            self.event.wait(timeout=1)

            print("thread is running.")


        # while not self.event.isSet():
        #     print(" thread is ready")
        #
        # self.event.wait()
        #
        # while self.event.isSet(): pass


if __name__ == '__main__':


    """
    event 标志默认为 False
    wait[timeout] 阻塞等待标志设置为True, timeout超时后停止阻塞
    set 设置标志为1
    claer 设置标志为False
    isSet()  返回标志状态
    
    """

    event = Event()
    for i in range(3):
        t = Thr(event)
        t.start()

    time.sleep(2)
    event.set()  # 设置为True , 放行

    event.clear() # 设置为False， 阻塞
