

# import asyncio
# import collections
# nums = collections.deque()
#
# async def put(nums):
#     n = 0
#     while n < 10:
#         n += 1
#         nums.appendleft(n)
#         print("put num ", n)
#         await asyncio.sleep(0.5)
#     else:
#         nums.appendleft(None)
#
#
# async def get(nums):
#     while 1:
#         if len(nums) == 0:
#             await asyncio.sleep(2)
#         else:
#             n = nums.pop()
#             if not n:
#                 break
#             print("get fun ", n)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait([get(nums), put(nums)]))


# import asyncio
#
#
# async def read(a):
#     # asyncio.sleep(1)
#     print("read number:", a)
#
#
# def run():
#     for i in range(10):
#         loop.run_until_complete(read(i))


# loop = asyncio.get_event_loop()
# if __name__ == "__main__":
    # run()

class a():
    def foo(self):
        print("in a")

class b(a):
    def foo(self):
        super(b, self).foo()
        print("in b")

class c(a):
    def foo(self):
        super(c, self).foo()
        print("in c")

class d(b,c):
    def foo(self):
        super().foo()
        print("in d")

dd = d()
dd.foo()