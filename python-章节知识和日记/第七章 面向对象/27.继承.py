
# class Animal:

#     def __init__(self, name, age, gender):
#         self.name = name 
#         self.age = age 
#         self.gender = gender

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, name):
#         self.__name = name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         self.__age = age
    
#     @property
#     def gender(self):
#         return self.__gender
    
#     @gender.setter
#     def gender(self, gender):
#         self.__gender = gender
    
#     def __str__(self):
#         return f"{self.__class__.__name__}({self.__dict__})"

class GeneratorProperty:
    """在 类中 __fields__ 定义 数据转成 属性"""
    def __new__(cls, *args, **kwargs):
        # 获取 当前类的 类属性 __fields__ 
        fields = cls.__fields__
        # 遍历 所有的 fields 、给 类 添加 property 属性
        for field in fields:
            name = f"_{cls.__name__}__{field}"
            # 生成 field 的 getter 方法 和 setter 方法
            getter = (lambda x: lambda self: getattr(self, x))(name)
            setter = (lambda x: lambda self, y: setattr(self, x, y))(name)
            # 生成 property 属性 
            prop = property(getter, setter) 
            # 给 当前类 添加 类属性、 属性名 是 field, 属性 值是 prop
            setattr(cls, field, prop)
        def repr(self):
            prefix = f"_{self.__class__.__name__}__"
            dct = {k.removeprefix(prefix):v for k, v in self.__dict__.items()}
            return f"{self.__class__.__name__}({dct})"
        # 给类添加 __repr__ 魔术方法 
        setattr(cls, "__repr__",  repr)
        # 创建 类的 对象 
        instance = super().__new__(cls) 
        # 遍历 所有的 fields、 完成属性的初始化 (给对象添加属性)
        for field in fields:
            setattr(instance, field, kwargs.get(field))
        # 将创建的对象 返回 (返回的对象已完成属性的初始化操作)
        return instance
class Animal(GeneratorProperty):

    __fields__ = ("name", "age", "gender")

   

if __name__ == "__main__":
    
    anl = Animal(name="小黑", age=2)

    anl.age = 10
    # anl.gender = "女"

    print(anl.name)
    print(anl.age)
    print(anl.gender)

    print(anl)