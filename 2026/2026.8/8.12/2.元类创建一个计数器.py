"""
【元类】 使用元类创建一个计数器，跟踪类的实例数量。
要求： 创建一个名为 CountingMeta 的元类，它需要：

1.  跟踪使用该元类创建的所有类的实例数量。

2.  元类中提供一个静态方法 get_instance_count(cls)，返回某个类的实例数量。

3.  创建一个类 Example，使用 CountingMeta 作为其元类。

创建多个 Example 实例，并验证 CountingMeta 能正确返回实例数量。
"""
class CountingMeta(type):
    # 保存每个类的实例数量
    instance_counts = {}

    def __new__(mcs, name, bases, namespace):
        # 创建类
        cls = super().__new__(mcs, name, bases, namespace)

        # 初始化该类的实例数量
        mcs.instance_counts[cls] = 0

        return cls

    def __call__(cls, *args, **kwargs):
        # 当 Example() 被调用时，会执行这里
        instance = super().__call__(*args, **kwargs)

        # 对当前类的实例数量 +1
        CountingMeta.instance_counts[cls] += 1

        return instance

    @staticmethod
    def get_instance_count(cls):
        return CountingMeta.instance_counts.get(cls, 0)


class Example(metaclass=CountingMeta):
    pass


# 创建实例
a = Example()
b = Example()
c = Example()

# 查看实例数量
print(CountingMeta.get_instance_count(Example))