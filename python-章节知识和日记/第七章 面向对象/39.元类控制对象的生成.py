"""
使用元类 控制 对象的创建 实现单例模式

元类 是 类的 类型

元类 中的 __new__ 魔术方法 是用来 创建类的

元类 中的 __init__ 魔术方法 是用来 给 类 做初始化的

元类 中的 __call__ 魔术方法 是用来 创建 类的对象

"""


class Singleton(type):
    """用来控制类的对象、永远返回一个对象"""

    def __call__(self, *args, **kwargs):
        # 判断 当前类 中 是否已经存在 对象
        if not hasattr(self, "_instance"):
            # 怎么创建对象
            instance = super().__call__(*args, **kwargs)
            # 将 创建的对象 和当前类 进行绑定
            setattr(self, "_instance", instance)

        return getattr(self, "_instance")


class Sun(metaclass=Singleton):
    pass


if __name__ == "__main__":
    s = Sun()
    s1 = Sun()

    print(s)
    print(s is s1)
