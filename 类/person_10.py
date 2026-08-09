# class Person:
#     def lastName(self): ...
#     def giveRaise(self): ...
#     def __repr__(self): ...
#
# class Manager(Person):          # 继承
#     def giveRaise(self, …): …   # 定制
#     def someThingElse(self, …): …   # 扩展
#
# pat = Manager()
# pat.lastName()                  # 原样继承
# pat.giveRaise()                 # 定制的版本
# pat.someThingElse()             # 在这里扩展
# print(pat)                      # 继承的重载方法
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
class Manager(Person):
      # 子类自己的构造：只需 name 和 pay
    def __init__(self, name, pay):
        # 手动运行父类构造，固定 job='mgr'
        Person.__init__(self, name, 'mgr',pay)
    def giveRaise(self, percent,bonus = .10):
        Person.giveRaise(self, percent+bonus)
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    # job 名由类自动设置 两个参数就够了，job 自动为 'mgr'
    pat = Manager('Pat Jones', 50000 )
    pat.giveRaise(.10)
    print(pat.lastName())
    print(pat)


