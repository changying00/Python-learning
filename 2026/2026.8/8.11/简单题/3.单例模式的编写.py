#【单例模式】使用多种方式、完成 单例模式代码的编写
# class Singleton:
#
#     _instance = None
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
# a = Singleton()
# b = Singleton()
#
# print(a)
# print(b)
# print(a is b)

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Person(Singleton):
    def __init__(self, name):
        self.name = name

p1 = Person("张三")
p2 = Person("李四")

print(p1 is p2)