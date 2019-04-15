"""
装饰器：在不改变原函数的情况下给函数增加功能
装饰器由闭包和语法糖
"""

def check(fun):
    # print(type(fun), fun.__name__)
    # fun()


    def ck():
        user = input("请输入用户名")
        if user == "kwx":
            fun()
        else:
            print("没有此权限")
    return ck


@check
def selecctgoods():
    print("11111")

@check
def insertorder():
    print("插入订单")

"""
解释器解释到有装饰的函数：会改变函数结构
把函数作为参数传给装饰器，并且执行装饰器的返回值(装饰器)
"""