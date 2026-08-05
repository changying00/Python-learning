"""
俩个 对象 如果 要比较 内容、使用'=='

自定义的类 如果要想比较2个对象 内容是否相同、必须 提供 魔术方法__eq__

__eq__魔术方法 默认 比较的是 2个对象的地址

如果 希望 比较 内容、则 必须 自己编写 比较规则~

俩个对象 比较 内容的 规则是

    1.比较2个对象的 地址 是否相同、 如果相同、则直接返回 True

    2.判断other 是否为空或者 非当前类

    3.逐个属性、进行比较
"""
class Human:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self,other):
        if self is other:
            return True
        if other is None or not isinstance(other,self.__class__):
            return False
        return self.name == other.name and self.age == other.age

class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age
if __name__ == "__main__":
    #创建一个 人类 对象
    p1 = Human('张三',20)
    #创建一个 人类对象
    p2 = Human('张三',20)


