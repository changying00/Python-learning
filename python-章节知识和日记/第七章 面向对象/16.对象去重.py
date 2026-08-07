class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __eq__(self, value: object, /) -> bool:
        if self is value:
            return True

        if value is None or not isinstance(value, self.__class__):
            return False

        return self.name == value.name and self.age == value.age

    def __hash__(self) -> int:
        """
        返回 一个 对象的 hash值

        一个 对象 它的 hash 值 遵循一个原则:
            内容相同的对象 hash 值 一定 相同 、 内容不同的 对象 hash 值 尽可能的 不同
        """
        # 将 所有的属性值 存储到元组中， 最对元组 进行 hash 运算 ~~
        return hash((self.name, self.age))


if __name__ == "__main__":
    # set 集合 存储的数据 必须是 可hash 的 、
    # set 去重的原理 :  hash值相同、且 内容相同 才会去重

    dog_sets = {Dog("小黑", 2), Dog("小白", 3), Dog("小黑", 2)}

    print(dog_sets)