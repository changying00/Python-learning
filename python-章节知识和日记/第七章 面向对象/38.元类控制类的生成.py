"""
什么是 元 类 :

    元类是 类的 类型、 类是 元类的 对象 !

    type : type 是所有类的起源、所以 type 也被称为 元类 。

一个类 创建的 实例 叫 对象 、 万物皆为对象，  可以将 一个类 理解为 一个对象，那么 类的 类型是 type 。


元类 可以做什么

    a) 创建类

    b) 控制类的创建

    c) 控制对象的创建


type 它的 2 个作用

    a) 查看一个数据的类型

    b) 创建类

    type(cls, name: str, bases: tuple, namespace: dict)

        name : 设置要创建的 类的名字
        bases : 设置 类 继承的 父类 元组
        namespace : 设置 类中的 属性 和 方法

"""


class Animal:

    def __init__(self, age):
        self.age = age

    # class Dog(Animal):


#     def __init__(self, name, age):
#         self.name = name
#         super().__init__(age)

# 使用 type 创建一个 Dog类 、且 Dog 要求 继承 Animal 类 、 且 Dog 中 有 1 个属性 name

def init(self, name, age):
    self.name = name
    Animal.__init__(self, age)


# 创建一个类
Dog = type("Dog", (Animal,), {"__init__": init})

# 创建一个 Dog 对象
dog = Dog("小黑", 2)

print(dog.name, dog.age)

# if __name__ == "__main__":

#     dog = Dog()

#     print(type(dog))

#     print(type(Dog))

#     print(type(type))

