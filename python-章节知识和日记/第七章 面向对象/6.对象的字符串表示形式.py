"""
对象 的 字符串表示 形式 :

打印 一个 对象、 本质 上 就是 获取 这个对象的 字符串表示形式

print(dog) ==>  print(str(dog))

__str__  :   使用 字符串的形式 表示对象,  当 打印对象的时候，以更加优雅方式进行展示

    如果 对象 存储到 容器中， 打印容器的时候， 仍旧会显示 对象的地址表示形式


__repr__ :  可以解决 对象在 容器中 打印显示地址的问题

    HomeDog("哈巴狗", 3)  ====>  eval 函数 可以 将 HomeDog("哈巴狗", 3) 格式的字符串 直接转成 对象

"""
class HomeDog:
    """家狗"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self) -> str:

    #     # 获取 当前类的 名字  self.__class__.__name__
    #     # 获取 当前对象的所有 属性 self.__dict__  (返回一个 字典格式的数据)
    #     return f"{self.__class__.__name__}({self.__dict__})"

    def __repr__(self) -> str:

        return f"{self.__class__.__name__}({self.__dict__})"


if __name__ == "__main__":

    # 创建一个 HomeDog对象
    dog = HomeDog("哈巴狗", 2)
    # 打印 一个对象、 默认输出 这个对应的 地址
    #  默认输出 格式 :  模块 + 类型 object + 地址
    print(dog)

    # print(dog.name,  dog.age)
    # print(x)

    dog_list = [HomeDog("哈巴狗", 2),  HomeDog("土狗", 3), HomeDog("小黑", 2), HomeDog("大黄", 3)]

    print(dog_list)