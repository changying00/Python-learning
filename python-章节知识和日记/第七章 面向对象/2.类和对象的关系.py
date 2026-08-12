"""
类 :  是 自然界中 具有 相同特征 和 行为  的事物统称 。

研究一个类 、主要 研究 这个类中的 特征 (属性) 和 行为 (方法)

使用 关键字 class 定义 自然界中 类型

语法:

class <ClassName>:
    pass


ClassName 是一个 标识符、需要遵循标识符命名规则、类名采用 大驼峰命名法 ~~~

狗有什么特征 :

    肤色 skin，  品种 kind， 年龄 age， 性别 gender

狗有什么行为 :

    叫 call

    吃 eat

    ...



类 是 对象 的模板 （告诉对象 你有什么属性 和 方法）

对象 是 类的 具体实现


"""
class Dog:
    """
    定义一个 Dog 类 、描述自然界中的 狗
    """
    def __init__(self):
        """
        在 __init__ 魔术方法中 可以 定义 类的属性
        self :  代表 当前类的对象
        """
        # 给 Dog 类 添加一个 肤色 属性 、值为 黄色
        self.skin = "黄色"
        # 给 Dog 类添加一个 品种 属性、值为 中华田园犬
        self.kind = "中华田园犬"
        # 给 Dog 类 添加一个 年龄属性 、值为 0
        self.age = 0
        # 给 Dog 类 添加一个 性别属性、 值为 公
        self.gender = "公"

    def eat(self):
        """
        狗的 吃行为
        """
        print(f"肤色为{self.skin}的狗正在吃东西")

    def call(self):
        """
        狗的 叫行为
        """
        print(f"{self.kind}正在汪汪汪的叫")


if __name__ == "__main__":

    # 通过 类 来 创建一个 该类的对象
    # 使用 类 来创建 对象， 会自动 调用 类中的 __init__ 魔术方法 ！
    # 完成 属性 的创建 和 赋值 (初始化)
    dog = Dog()

    print(dog, type(dog),  isinstance(dog, Dog))

    # 获取 dog 的肤色
    print(dog.skin)
    # 获取 dog 的品种
    print(dog.kind)
    # 更改狗的颜色
    dog.skin = "黑色"
    # 输出更改的 狗额肤色
    print(dog.skin)

    # 调用 狗的 eat 方法
    dog.eat()

    # 调用 狗的 叫的行为
    dog.call()