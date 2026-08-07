"""
单例模式 :

    一个类 只能 创建有且只有 1 个对象 。

"""


class Sun:

    def __new__(cls, *args, **kwargs):
        # 判断 当前 类 是否 有一个属性 _instance
        if not hasattr(cls, "_instance"):
            # 没有创建过对象、 则 创建一个对象
            instance = super().__new__(cls)
            # 将 创建的 对象 和 当前类 进行绑定
            setattr(cls, "_instance", instance)
        # 返回 当前类绑定的 唯一对象
        return getattr(cls, "_instance")


if __name__ == "__main__":

    s1 = Sun()
    s2 = Sun()

    print(s1 is s2)
    print(s1)
    print(s2)
