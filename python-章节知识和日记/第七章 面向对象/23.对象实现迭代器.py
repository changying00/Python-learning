"""

    __iter__  :   让对象做成可迭代的

    __next__  :   允许使用 next 函数 获取 迭代器中的数据


"""
from typing import Iterator


class Collection:

    def __init__(self):

        self.__array = []

    def push(self, *args):
        for v in args:
            self.__array.append(v)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__array})"

    def __iter__(self):
        return self

    def __next__(self):
        """每次使用 next 函数 从迭代器中获取数据、就相当 调用 __next__ 魔术方法"""
        # 删除 列表中的 第一个元素
        if len(self.__array) == 0:
            # 迭代器 当数据 取完 后 必须 抛出 StopIteration 错误
            raise StopIteration

        return self.__array.pop(0)


if __name__ == "__main__":

    col = Collection()

    col.push(10)
    col.push(20)
    col.push(30)
    col.push(40)
    col.push(50)

    for v in col:
        print(v)

    # print(isinstance(col, Iterator))

    # print(next(col))
    # print(next(col))
    # print(next(col))
    # print(next(col))
    # print(next(col))

    # print(next(col))

