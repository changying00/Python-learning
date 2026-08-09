"""（同时支持导入和运行/测试）"""
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

if __name__ == '__main__':          # 仅当作为脚本运行（__name__ 为 '__main__'）时执行
    bob = Person('Bob Smith')       # 创建实例
    sue = Person('Sue Jones', job='dev', pay=100000)  # 关键字传参
    print(bob.name, bob.pay)        # 打印 bob 的属性
    print(sue.name, sue.pay)        # 打印 sue 的属性