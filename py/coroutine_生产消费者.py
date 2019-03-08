



import collections

nums = collections.deque()


def put(nums):

    for i in range(10):
        print("put num :", i)
        nums.appendleft(i)
        yield
    nums.appendleft(None)




def get(nums, gen):

    gen.send(None)

    while 1:
        
        try:
            n = nums.pop()
            if n is None:
                break
            print("get fun->: ", n)
            n = next(gen)
        except StopIteration:
            pass
        

if __name__ == "__main__":

    g = put(nums)
    get(nums, g)
    print(nums)
