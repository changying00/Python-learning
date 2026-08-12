"""

__init__ :   初始化类中定义的属性

__del__  :   当 对象 被销毁的时候 执行的 方法

"""
class Human:

    def __init__(self, name, age):
        print("=====================init================")
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃饭")


    def __del__(self):
        print("=====================del(销毁)===================")


if __name__ == "__main__":

    # 打印 一个类 、不会调用 __init__
    print(Human)

    # 创建一个对象， 会自动调用 __init__
    p = Human("张三", 20)

    # 销毁对象
    del p

    input()


