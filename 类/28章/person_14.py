"""
记录并处理关于人的信息。
直接运行此文件可测试其类。
"""
# 使用通用显示工具
from classtools import AttrDisplay
#混入显示能力：Person 的 MRO 变为 # [Person, AttrDisplay, object]
class Person(AttrDisplay):  # 在这一层混入 repr 显示
    """创建并处理人的记录"""
    def __init__(self,name,job = None,pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay = int(self.pay * (1 + percent))
 # MRO: [Manager, Person, AttrDisplay, object]
class Manager(Person):
    """有需求的定制版Person"""
    def __init__(self,name,pay):
        Person.__init__(self,name,"mgr",pay)#job 名字固定
    def giveRaise(self,percent,bonus = .10):
        Person.giveRaise(self,percent+ bonus)

if __name__ == "__main__":
    # bob = Person('Bob Smith')
    # sue = Person('Sue Jones', job='dev', pay=100000)
    # print(bob)
    # print(sue)
    # print(bob.lastName(), sue.lastName())
    # sue.giveRaise(.10)
    # print(sue)
    # pat = Manager('Pat Jones', 50000)
    # pat.giveRaise(.10)
    # print(pat.lastName())
    # print(pat)

    print(Person.__name__)
    print(Person.__dict__)

    print(Person.__class__)
    print(Person.__mro__)
    print(Person.__bases__)