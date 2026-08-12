"""
__new__ :  负责创建对象的

对象的创建过程 :

    1. 先调用 子类的 __new__ 魔术方法 创建 对象

    2. 子类的 __new__ 会 使用 super().__new__(cls) 委托父类 创建对象

    3. 父类 继续 向上委托 它的父类、直到 找到 object 为止 创建对象

    4. 父类创建的对象 会返回给 子类、 并执行 子类的 __init__ 魔术方法

    5. 子类 __init__ 魔术方法 会 调用 super().__init__(*args, **kwargs) 进行父类属性的初始化

    6. 父类中的 __init__ 继续 初始化它的 父类属性、直到找到 object 为止

    7. 父类属性初始化完成后、继续 初始化 子类对应的 属性

"""


class Animal:

    def __new__(cls, *args, **kwargs):
        # 负责创建一个对象
        return super().__new__(cls)

    def __init__(self, age):
        # super().__init__()  object 类中没有任何属性需要做初始化，所以 该行代码 可以省略 ！
        self.age = age


class VipDog(Animal):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, age):
        super().__init__(age)
        self.name = name


if __name__ == "__main__":
    anl = Animal()

    dog = VipDog("小黑", 2)