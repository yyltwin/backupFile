#!/usr/bin/env python
# -*- coding:utf-8 -*-


import bisect


# 用来处理已排序的序列， 维持已排序的序列， 升序
# 二分查找0

inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 6)
bisect.insort(inter_list, 1)

print(inter_list)    # >> [1, 2, 3, 5, 6]

# bisect.insort 将元素插入到序列中
# bisect.bisect 返回 元素应该插入在序列中的哪个位置, 默认bisect = bisect.bisect_right

bisect.bisect = bisect.bisect_left  # 更改有相同元素默认插入在左

print(bisect.bisect(inter_list, 3))


# 使用bisect 前需要先将原序列排序， 否则元素会混乱
a = [2,3,1]
bisect.insort(a, 5)
print(a)
