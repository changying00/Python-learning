"""


"""
class Dog:

    def __init__(self, skin, kind, age):
        # 初始化属性 并给属性赋值
        self.skin = skin
        # 初始化属性 并给属性赋值
        self.kind = kind
        # 初始化属性 并给属性赋值
        self.age = age


if __name__ == "__main__":

    dog = Dog("黄色", "田园犬", 2)

    print(dog.skin)
    print(dog.kind)

    print(dog.age)

    # 删除 dog 中的 肤色
    del dog.skin

    # 动态添加的属性
    dog.gender = "公"
    # 直接访问一个 不存在的属性、会抛出错误
    print(dog.gender, dog.skin)

    dog2 = Dog("黑色", "贵宾犬", 3)
    # dog 中动态追加的属性 dog2 无法使用 ~~~
    print(dog2.gender)


