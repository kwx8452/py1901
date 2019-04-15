"""
生成器
"""
import sys

list1 = (x for x in range(100))
print(sys.getsizeof(list1))
for x in list1:
    print(x)
print("结束")