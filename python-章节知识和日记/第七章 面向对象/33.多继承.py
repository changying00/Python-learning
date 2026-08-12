"""
Python 语言 采用 多继承 、一个类 允许 继承多个类 、多个被继承的类使用 逗号分隔即可！！！

"""


class A:

    def __init__(self, a):
        self.a = a

    def xyz(self):
        print("print-----------a")


class B:

    def __init__(self, b):
        self.b = b

    def abc(self):
        print("print-------------b")

    def xyz(self):
        print("print ---xyz ---- b")


class C(A, B):
    """
    C 类 继承了 A 和 B 两个类 、 C 是 A 的子类、 也是 B 的子类

    C 类 可以继承 A 类中的定义的 属性和方法
    C 类 也可以继承 B 类中 定义的属性和方法
    """

    def __init__(self, a, b):
        # 给 父类中的属性赋值
        super().__init__(a)
        # 初始化 B 类中的 属性
        B.__init__(self, b)


if __name__ == "__main__":
    c = C("a", "b")

    print(c.a, c.b)

    B.xyz(c)



