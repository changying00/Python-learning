"""
成员方法:  和 对象有关的 方法、它可以使用 对象 进行调用、 成员方法 也支持使用类调用 但不推荐

==============================================================================================

静态方法:  和 类有关的 方法、和 对象 没有直接 关系 。静态方法 通过 类进行调用， 也支持使用 对象调用但不推荐。

    在 方法 的上面 添加 装饰器 @staticmethod 、被修饰的方法 不需要 在提供 self .

类方法 :  和 类有关的 方法 , 本质上 和 静态方法作用相同

    在 方法上 使用 @classmethod 装饰器、 被装饰的方法 必须提供 cls 作为 第一个参数

    cls 代表 当前类

===============================================================================================

如果 一个类 它里面所有的方法 都是 静态/类 方法 、那么 这个类 也被称为  工具类 。


"""


class Dog:

    def eat(self):
        print("小狗正在吃饭!!!")


class Calc:
    """计算器类"""

    @staticmethod
    def mul(a, b):
        """乘积"""
        return a * b

    @staticmethod
    def sub(a, b):
        """差"""
        return a - b

    @staticmethod
    def sum(a, b):
        """和"""
        return a + b

    @staticmethod
    def div(a, b):
        """商"""
        return a / b

    @staticmethod
    def mod(a, b):
        """余数"""
        return a % b

    @classmethod
    def divmod(cls, a, b):
        """整除求商和约束"""
        return a // b, cls.mod(a, b)


if __name__ == "__main__":

    # 创建一个对象
    # dog = Dog()
    # # 调用 方法
    # dog.eat()
    # # Dog.eat(dog)

    # 创建一个对象
    # calc = Calc()
    # print(Calc.mul(3, 5))

    print(Calc.divmod(6, 4))
