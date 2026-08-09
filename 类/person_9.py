"""
（在子类中添加方法定制）
"""
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return f'[Person:{self.name} ${self.pay:,}]'
#定义了一个名为 Manager 的新类，它继承自超类 Person，并可能对它做定制
class Manager(Person): #定义Person的子类
    def giveRaise(self, percent,bonus= .10):#重定义 以定制
        # self.pay = int(slef.pay * (1 + percent + bonus))# 坏做法：剪切粘贴
        Person.giveRaise(self, percent + bonus)   # 调用 Person 的版本 # 好做法：增强原版

if __name__ == '__main__':
        bob = Person("Bob Smith")
        sue = Person("Sue Jones",job = 'dev',pay = 100000)
        print(bob)
        print(sue)
        print(bob.lastName(),sue.lastName())
        sue.giveRaise(.10)
        print(sue)
        # 创建 Manager：自动运行 __init__
        pat = Manager('Pat Jones','mgr',50000)

        pat.giveRaise(.10) # 运行定制版本
        print(pat.lastName())# 运行继承来的方法
        print(pat)  # 运行继承来的 __repr__
        print("---all three---")
        #两次涨薪的累积效果
        for obj in (bob,sue,pat): # 通用地处理对象
            obj.giveRaise(.10) # 运行这个对象的 giveRaise 每次迭代都重新做继承查找，按类型选版本
            print(obj)# 运行共同的 __repr__