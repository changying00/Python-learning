"""
【魔术方法】我们有一个简单的Person类，代表一个人，其中包含姓名和年龄。 要求如下：
A) 打印 人类对象的时候， 会自动显示 对应的姓名和年龄
B) 两个人类对象 可以使用 == 比较内容，且 名字和年龄如果相同，则认为是相同的
C) 将多个对象存储到 Set集合中时候，可以根据 姓名+年龄 去重、姓名+年龄 不允许相同。
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))


if __name__ == "__main__":
    p1 = Person("张三", 20)
    p2 = Person("张三", 20)
    p3 = Person("李四", 25)
    print(p1)
    print(p1 == p2)
    print(p1 == p3)
    s = {p1, p2, p3}
    print(s)
