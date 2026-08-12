"""
抽象类:  有抽象方法的类被称为抽象类、 抽象类不能创建对象

如果 一个类 中 有些 方法 只是用来 制定规则，没有具体的实现 、那么 这些 方法 可以做成 抽象方法

    abc.@abstractmethod

如果 一个类 中 包含 抽象方法， 那么 这个类 必须做成 抽象类 。

    抽象 类 继承 abc.ABC


如果 一个类 继承了抽象类 、那么这个类 必须重写 抽象类中 所有的抽象方法 、否则 这个类 也是一个抽象类

"""
from abc import abstractmethod, ABC


class Shape(ABC):
    """
    图形类
    """

    @abstractmethod
    def premiter(self):
        """周长"""
        pass

    @abstractmethod
    def area(self):
        """面积"""
        pass


class Circle(Shape):

    def __init__(self, r):
        self._r = r

    def premiter(self):
        return 3.14 * 2 * self._r

    def area(self):
        return 3.14 * self._r ** 2


if __name__ == "__main__":
    shape = Circle(5)

    print(shape.premiter())
    print(shape.area())

