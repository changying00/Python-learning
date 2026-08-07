"""
【魔术方法】编写一个类 A, 提供一个 value 属性 ，该类 创建的 对象 能够 让 下面的 表达式 返回 True
 a + 1 == 2  and a + 1 == 3
 表达式中的 a 是 类 A 的实例对象
"""


class A:
    def __init__(self):
        self.value = 1

    def __add__(self, other):
        result = self.value + other
        self.value += 1
        return result


if __name__ == "__main__":
    a = A()
    print(a + 1 == 2 and a + 1 == 3)
