class name(superclass,…):    # 赋值给 name——类体执行完，类对象绑定到 name
    attr = value             # 共享的类数据——挂在类对象上，所有实例共享
    def method(self,…):      # 方法——也是类属性，只是恰好是函数
        self.attr = value    # 每个实例各自的数据——挂在实例对象上
x = name(…)                  # 创建一个实例（若定义了 __init__ 则触发之）
x.method(…)     # 调用一个方法（自动把 x 传进 self）

# print(name.__dict__)
# print(name.__class__)
# print(name.__mro__)
# print(x.__dict__)
# print(name.__bases__)