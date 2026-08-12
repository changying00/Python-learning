"""假入有一个类、且该类中 定义了多个 类属性， 现要求编写一个元类、实现将类中的类型的类属性
全部更改为 大写属性，例如
class A:
	name = “a”
	sex  = “m”
经过元类处理后，A.NAME 能够输出 a , A.SEX 能够输出 m"""
class UpperMeta(type):

    def __new__(mcs, name, bases, namespace):

        # 遍历类的命名空间
        for key, value in list(namespace.items()):

            # 如果属性值是字符串
            if isinstance(value, str):
                # 原来的属性删除
                del namespace[key]

                # 属性名改成大写
                namespace[key.upper()] = value

        # 创建类
        return super().__new__(mcs, name, bases, namespace)


class A(metaclass=UpperMeta):
    name = "a"
    sex = "m"


print(A.NAME)
print(A.SEX)