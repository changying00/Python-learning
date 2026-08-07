"""
【魔术方法】使用单例模式、完成一个 Sington 类的定义。
"""


class Sington:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name=None):
        if not hasattr(self, "_initialized"):
            self.name = name
            self._initialized = True


if __name__ == "__main__":
    a = Sington("A")
    b = Sington("B")
    print(a is b)
    print(a.name)
