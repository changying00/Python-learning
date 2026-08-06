class Human:

    def __init__(self, name, age):
        # 将 name 传给 了 property 属性 name
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"{self.__class__.__name__}({self.__dict__})"


if __name__ == "__main__":
    p = Human("小明", 20)
    print(p)




