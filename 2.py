class AA(object):
    # 类属性
    isAlive = False
    def __init__(self, _hp, _mp):
        # 实例属性
        self.hp = _hp
        self.mp = _mp


class BB(object):
    # 类方法
    def __init__(self, _speed):
        # 实例方法
        self.speed = _speed

    def run(self):
        # 声明类方法run
        print("run速度为%d" % self.speed)

    # 声明静态方法
    @staticmethod
    def dead():
        print("BB死亡")

    # 声明类方法
    @classmethod
    def printclassinfo(cls):
        print("类文档%s" % cls.__doc__)




if __name__ == "__main__":
    # 对象通过类名传参给实例属性
    a = AA(10, 20)
    b = AA(50, 60)
    print(a.hp, b.mp)
    # 实例可以调用类属性
    print(a.isAlive)
    print(AA.isAlive)


    # 通过类名传参给实例方法
    c = BB(20)
    # 变量调用类方法
    c.run()
    # 变量调用静态方法
    c.dead()
    c.printclassinfo()
    BB.dead()