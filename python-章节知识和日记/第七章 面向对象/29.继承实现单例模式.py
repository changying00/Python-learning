"""
单例: 一个类 只能创建 1 个对象

"""


class Singleton:

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, "_instance"):
            # 创建一个 当前类的对象
            instance = super().__new__(cls)
            # 将 对象 和 当前类进行绑定
            setattr(cls, "_instance", instance)

        return getattr(cls, "_instance")


class Animal(Singleton):

    pass


if __name__ == "__main__":

    anl = Animal()
    anl2 = Animal()

    print(anl is anl2)
