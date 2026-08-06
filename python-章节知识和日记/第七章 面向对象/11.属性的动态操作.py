"""
已知 一个对象 它的属性名、 怎么 获取 它的属性值

    注意： 不能直接使用 . 调用 、因为 . 后面调用的是属性/方法， 而不是属性名 或者 方法名

    getattr :  获知 指定对象 属性名 对应的 属性值 、如果找不到，默认抛出错误、但 支持设置 默认值 。

        getattr(obj, name, default?) :  获取 obj 对象中 name 属性名 对用的 属性值


已知 一个 键 和 值 2个数据 、怎么 将它做成 对象的 属性 和 属性值

已知 属性名 和 属性值 、怎么 动态追加到对象中

    setattr(obj, name, value) :  给 obj 对象 绑定 属性 name 且值为 value


如何 判断 一个对象中 是否存在 某个属性名

    hasattr(obj, name) :  判断  obj 对象中 是否存在 name 属性名

如何 根据 属性名 删除 一个对象的 属性

    delattr(obj, name)

【类的组成】编写一段代码，判断 某个对象 是否存在 指定的方法，如果 存在，则 获取该方法，否则 给对象添加一个方法，并返回 添加的 方法
"""

class Dog:

    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


if __name__ == "__main__":
    # 创建一个dog对象
    dog = Dog(2)
    # 已知 dog 对象中 有一个属性 、它的名字 叫 age , 怎么 获取它的值
    # print(dog.age)
    print(getattr(dog, "age", 0))

    key = "name"
    value = "小黑"

    # 怎么 给 dog 对象 添加一个属性 将 key 的值 作为属性、将 value 值作为 为 属性值
    # dog.name = "小黑"
    setattr(dog, key, value)
    print(dog.__dict__)

    # 判断 dog 是否 有 一个属性、他的名字叫 age
    print(hasattr(dog, "age"))

    delattr(dog, "age")


