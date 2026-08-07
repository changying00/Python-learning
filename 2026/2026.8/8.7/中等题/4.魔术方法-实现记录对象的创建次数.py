"""
【魔术方法】编写一个类、 提供一个类属性 instance_count, 记录对象创建的次数，设计类的 __new__ 魔术方法、实现能够记录 对象的创建的次数
"""


class Counter:
    instance_count = 0

    def __new__(cls, *args, **kwargs):
        cls.instance_count += 1
        return super().__new__(cls)

    def __init__(self, name=""):
        self.name = name


if __name__ == "__main__":
    a = Counter("a")
    b = Counter("b")
    c = Counter("c")
    print(Counter.instance_count)
