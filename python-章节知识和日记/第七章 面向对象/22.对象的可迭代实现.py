"""
如何 让 一个 对象 做成 可迭代对象

    __len__  :  获取 长度

    __iter__ :  将 对象 做成 可迭代的


"""


class Collection:
    """
    存储多个数据的容器
    """

    def __init__(self):
        # 定义一个空列表 进行数据存储
        self.__array = []

    def push(self, *args):
        for v in args:
            self.__array.append(v)

    def get(self, index):
        return self.__array[index]

    def __str__(self):
        return f"{self.__class__.__name__}({self.__array})"

    def __len__(self):
        return len(self.__array)

    def __iter__(self):
        """使用 yield 每次返回一个数据 """
        for v in self.__array:
            yield v


if __name__ == "__main__":

    col = Collection()
    # 向容器 中添加数据
    col.push(10)
    col.push(20)
    col.push(30, 40, 50, 60)

    for v in col:
        print(v)

    print("=======================")

    for v in col:
        print(v)