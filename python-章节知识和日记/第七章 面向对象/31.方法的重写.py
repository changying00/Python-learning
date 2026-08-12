"""
 方法重写(覆盖):
     如果 父类 中 提供的 方法 不满足 子类的 需求 , 子类 可以 重写 父类中定义的方法

如果 父类 中提供的 方法 满足 子类的 部分需求 、子类 仍旧需要 重写父类中的方法
    此时 子类 可以使用 super 关键字 调用 父类中的 方法

"""


class Animal:
    """
    动物类
    """

    def __init__(self, age):
        self.age = age

    def eat(self):
        print(f"{self.age}岁的动物正在吃饭！")


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(age)
        self.name = name

    def eat(self):
        print("小狗在吃骨头")


class Cat(Animal):

    def __init__(self, age, gender):
        super().__init__(age)
        self.gender = gender

    def eat(self):
        # 调用 父类中的 eat 方法， 完成部分需求
        super().eat()
        print("小猫在吃鱼")


if __name__ == "__main__":
    dog = Dog("小黑", 2)
    dog.eat()

    cat = Cat(2, "公")
    cat.eat()