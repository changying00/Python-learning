"""
简单题 魔术方法】编写一个 Num 类、 该类 有一个属性 value , 要求如下
a) 私有化属性
b) 两个 Num 对象 允许 做 加法运算 ，例如 Num(2) +  Num(3)   会返回 一个新的Num对象，且值 为5
c) 两个 Num 对象 允许 做 减法运算
d) 两个 Num 对象 允许做 乘法运算
e) 两个 Num 对象 允许做 除法运算
f) 两个 Num 对象 允许做 整除运算
g) 两个 Num 对象 允许做 求余数运算
h) 打印 Num 对象的时候，显示 格式如：Num(4)
"""


class Num:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __add__(self, other):
        return Num(self.__value + other.__value)

    def __sub__(self, other):
        return Num(self.__value - other.__value)

    def __mul__(self, other):
        return Num(self.__value * other.__value)

    def __truediv__(self, other):
        return Num(self.__value / other.__value)

    def __floordiv__(self, other):
        return Num(self.__value // other.__value)

    def __mod__(self, other):
        return Num(self.__value % other.__value)

    def __str__(self):
        return f"Num({self.__value})"

    def __repr__(self):
        return f"Num({self.__value})"


if __name__ == "__main__":
    a = Num(2)
    b = Num(3)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(Num(10) // Num(3))
    print(Num(10) % Num(3))
