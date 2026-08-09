"""运算符重载"""
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):                         # 行为方法
        return self.name.split()[-1]            # self 是隐含的操作对象
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # 只能在这里改
    def __repr__(self):   # 新增的方法
        return f'[Person:{self.name} ${self.pay:,}]' # 要打印的字符串
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())       # 使用新方法
    sue.giveRaise(.10)                          # 而不是硬编码
    print(sue.pay)
    print(sue)  # print 优先找 __str__，没有则用 __repr__

