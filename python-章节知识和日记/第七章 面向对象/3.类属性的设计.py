"""
类 中 定义的 属性 和 方法 被 所有 对象共享, 但不共享属性值

"""

class Dog:

    def __init__(self, kind, skin=None):
        """
        将 dog 中的 肤色 和 品种 作为 参数
        """
        self.skin = skin
        self.kind = kind

    def call(self):
        print(f"肤色为{self.skin}的{self.kind}在汪汪汪叫")


if __name__ == "__main__":

    # 创建一个 Dog对象
    dog = Dog("雪橇犬")
    print(dog)
    dog.skin = "白色"
    print(dog.skin, dog.kind)

    # 创建一个 Dog 类的对象
    #  会自动 调用 __init__ 魔术方法
    dog = Dog("黄色", "中华田园犬")

    print(dog)
    print(dog.skin, dog.kind)
    dog.call()

    # 创建 一个 Dog 对象
    dog2 = Dog("黑色", "贵宾犬")
    print(dog2.skin, dog2.kind)
    dog2.call()
