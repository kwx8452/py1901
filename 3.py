import types
class AA(object):
    # 类方法
    def __init__(self):
        # 实例方法
        self.n=2
        pass
    # @staticmethod
    def move(self):
        print(',,,,,')

    def go(self):
        print("fdddddd")

# 定义类方法
@classmethod
def attack(cls):
    print("a")

# 定义静态方法
@staticmethod
def adead():
    print("b")

# 将类运行并赋值给变量
a = AA()
# 类名调用类方法
AA.attack = attack
AA.attack()
# 类名调用静态方法
AA.dead = adead
AA.dead()
a.move()
a.go()
# b = a.move
del AA.go
a.go()

# print(a.n)
# delattr(a, "move")
# a.move()


