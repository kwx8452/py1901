"""
类装饰器：用类装饰器
"""

# class Good():
#     def __init__(self):
#         print('构造调用')
#
#     def __call__(self, *args, **kwargs):


"""
可调用对象：类，函数，实例
"""

class Decor():
    def __init__(self, _f):
        if input('用户名') == "kwx":
            self.f = _f
            self.f()
        else:
            print('无权限')

    # def __call__(self):
    #     self.f()

@Decor
def fun():
    print("执行原始函数")

# d1 = Decor(fun)
# d1.f()
