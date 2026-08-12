"""
两个 对象 如果 要比较 内容 、使用  `==`

自定义的类 如果要想比较 2个对象 内容是否 相同、 必须 提供 魔术方法 __eq__

__eq__ 魔术方法 默认 比较的是 2 个对象的地址

如果 希望 比较内容， 则 必须 自己编写 比较规则 ~

两个对象 比较 内容的 规则是:

    1. 比较 2 个对象的 地址 是否相同， 如果相同， 则直接返回 True

    2. 判断 other 是否 为空 或者 非 当前类 、则直接返回 False

    3. 追个属性 进行比较

"""

class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):

        if self is other:
            return True

        if other is None or not isinstance(other, self.__class__):
            return False

        return self.name == other.name and self.age == other.age


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":

    # 创建一个 人类对象
    p1 = Human("张三", 20)

    # 创建一个人类对象
    p2 = Human("张三", 20)

    # 比较 这个对象 是否是同一个对象
    print(p1 is p2)

    # 比较 两个对象 它的 内容是否相同 、会 自动调用 __eq__ 魔术方法
    print(p1 == p2)

    # 创建 一个 p3 对象
    p3 = Dog("张三", 20)
    print(p3 == p1)