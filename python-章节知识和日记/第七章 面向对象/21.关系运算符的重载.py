"""
如何 让 对象 支持 比较 大小

    __gt__ :   >

    __ge__ :   >=

    __lt__ :   <

    __le__ :   <=

    __ne__ :   !=

    __eq__ :   ==

"""

class Dog:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __gt__(self, other: "Dog"):
        return self.__age > other.__age


if __name__ == "__main__":

    # 定义一个容器，用来存储多个 DOG 对象
    dogs = [
        Dog("小白", 2),
        Dog("小黑", 1),
        Dog("小花", 3),
        Dog("小兰", 2)
    ]

    # 按照 狗的年龄 进行从小到大排序
    dogs.sort()

    print(dogs)
