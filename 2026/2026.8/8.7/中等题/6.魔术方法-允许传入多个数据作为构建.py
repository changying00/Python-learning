"""
 【魔术方法】编写一个类 、该 类 允许传入多个数据作为构造对象的参数、要求如下
a)  该类创建的对象 支持 使用 for 循环遍历 得到传入的 数据
b)  两个 该类 的 对象 支持 加法运算 、且 能够实现 多个数据的合并。 并返回 该类的新对象
25分钟
"""


class MultiData:
    def __init__(self, *args):
        self._data = list(args)

    def __iter__(self):
        return iter(self._data)

    def __add__(self, other):
        if not isinstance(other, MultiData):
            return NotImplemented
        return MultiData(*(self._data + other._data))

    def __str__(self):
        return f"MultiData({self._data})"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    a = MultiData(1, 2, 3)
    b = MultiData(4, 5)
    for item in a:
        print(item, end=" ")
    print()
    c = a + b
    print(c)
    for item in c:
        print(item, end=" ")
    print()
