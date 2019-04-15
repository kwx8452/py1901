"""
时间消耗装饰qi
"""
import time

def timecount(f):
    def tc():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__,'消耗', end-start)
    return tc


@timecount
def getfromlist():
    list1 = [x for x in range(10000)]
    print(list1.index(9999))


@timecount
def getfromgeberator():
    g1 = (x for x in range(10000))
    index = 0
    while True:
        try:

            result = next(g1)
            if result == 9999:
                print(index)
            index += 1
        except StopIteration as e:
            print(e)
            break
getfromlist()
getfromgeberator()


