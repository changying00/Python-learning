"""
【元类】 使用元类创建一个计数器，跟踪类的实例数量。
要求： 创建一个名为 CountingMeta 的元类，它需要：

1.  跟踪使用该元类创建的所有类的实例数量。

2.  元类中提供一个静态方法 get_instance_count(cls)，返回某个类的实例数量。

3.  创建一个类 Example，使用 CountingMeta 作为其元类。

创建多个 Example 实例，并验证 CountingMeta 能正确返回实例数量。
"""