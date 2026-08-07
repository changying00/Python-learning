"""
列表 支持  +  和 *

不是 所有对象 都支持 算术运算， 如何 让自己的 对象 支持 算术运算

__add__  :  +

__sub__  :  -

__mul__  :  *

__truediv__ :  /

__floordiv__:  //

__mod__  :  %

__pow__  :   **


已知 一个 变量 a ,  请问 下面的表达式 是否能够返回 True, 如果可以， 怎么设计

    a + 1 == 2  and a + 1 == 3

        当 a + 1 计算完成 后 , 让 a 自增 1

"""


class A:

    def __init__(self, v):
        self.__value = v

    def __add__(self, n):
        ret = self.__value + n
        # 将 self.__value 自增 1
        self.__value += 1
        return ret


class Number:

    def __init__(self, value):
        self.__value = value

    def __add__(self, other: "Number"):
        # 返回一个 新的 Number 对象 、他们的值 做加法运算
        return self.__class__(self.__value + other.__value)

    def __mul__(self, other: "Number"):
        return self.__class__(self.__value * other.__value)

    def __str__(self):
        return f"{self.__class__.__name__}({self.__value})"


if __name__ == "__main__":
    # n1 = Number(3)
    # n2 = Number(5)

    # print(n1 + n2)  # Number(8)

    # print(n1 * n2)  # Numer(15)

    # 创建一个 对象
    a = A(1)

    print(a + 1 == 2 and a + 1 == 3 and a + 1 == 4 and a + 1 == 5)