"""（添加增量式自测代码）"""
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

bob = Person('Bob Smith')                        # 测试这个类：job/pay 用默认值
sue = Person('Sue Jones', job='dev', pay=100000) # 自动运行 __init__，关键字传参
print(bob.name, bob.pay)                         # 取出属性：访问实例的 __dict__
print(sue.name, sue.pay)                         # sue 和 bob 的属性不同