"""
【魔术方法】使用基于类的装饰器 实现 单例模式 !!!
"""


class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance


@Singleton
class Demo:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    a = Demo("A")
    b = Demo("B")
    print(a is b)
    print(a.name)
