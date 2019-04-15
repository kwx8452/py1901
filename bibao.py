"""
闭包：
函数的内部声明函数
外部函数返回内部函数的引用
内部函数可以访问外部函数局部变量
"""
def fun1(a):
    def fun2(b):
        nonlocal a
        a += 1
        return a+b
    return fun2

f1 = fun1(10)
print(f1(20))
print(f1(20))
print(f1(10))