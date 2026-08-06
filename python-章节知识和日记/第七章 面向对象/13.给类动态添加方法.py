class Animal:

    def __init__(self, name):
        self.name = name

    def call(self):
        print("动物在哇哇叫")


if __name__ == "__main__":
    # 创建一个 动物对象
    anl = Animal("小黑")

    # 判断 anl 中是否有 eat 方法
    if not hasattr(anl, "eat"):
        # 给 当前类动态添加一个方法
        setattr(Animal, "eat", lambda self: print(f"我是一个动态添加的 eat 方法、动物叫 {self.name}"))
        # setattr(anl, "eat", lambda : print(f"我是一个动态添加的 eat 方法、动物叫 {anl.name}"))

    func = getattr(anl, "eat")
    # 调用 方法
    func()