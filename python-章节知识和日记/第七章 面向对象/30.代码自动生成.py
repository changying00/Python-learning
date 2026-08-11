class GeneratorProperty:
    """在类中__fields__定义数据转为属性"""

    def __new__(cls, *args, **kwargs):
        # 获取当前类的类属性 __fields__
        fields = cls.__fields__

        # 遍历所有的 fields，给类添加 property 属性
        for field in fields:
            name = f"{cls.__name__}_{field}"

            # 生成 field 的 getter 方法和 setter 方法
            getter = (lambda x: lambda self: getattr(self, x))(name)
            setter = (lambda x: lambda self, y: setattr(self, x, y))(name)

            # 生成 property 属性
            prop = property(getter, setter)

            # 给当前类添加类属性，属性名是 field，属性值是 prop
            setattr(cls, field, prop)

        # 创建类的对象
        instance = super().__new__(cls)

        # 遍历所有的 fields，完成属性的初始化（给对象添加属性）
        for field in fields:
            setattr(instance, field, kwargs.get(field))

        # 将创建的对象返回（返回的对象已完成属性的初始化操作）
        return instance

class VipDog(GeneratorProperty):
    __fields__ = ("name","age")
    pass
if __name__ == '__main__':
    print(dir(VipDog))
    print(dir(GeneratorProperty))