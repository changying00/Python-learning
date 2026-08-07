"""
【魔术方法】编写一个类、要求该类的对象只允许创建5个、超出5个对象后报错
"""


class Limited:
    _count = 0
    _max = 5

    def __new__(cls, *args, **kwargs):
        if cls._count >= cls._max:
            raise RuntimeError(f"最多只能创建 {cls._max} 个对象")
        cls._count += 1
        return super().__new__(cls)

    def __init__(self, name=""):
        self.name = name


if __name__ == "__main__":
    objs = [Limited(f"obj{i}") for i in range(5)]
    print(f"已创建 {Limited._count} 个对象")
    try:
        Limited("extra")
    except RuntimeError as e:
        print(e)
