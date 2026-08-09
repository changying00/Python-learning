"""（添加方法以封装操作）"""
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        # 行为方法
        # self 是隐含的操作对象
    def lastName(self):  # 行为方法：self 是隐含的操作对象
        #不改变实例的属性使用return 返回新的不改变实例的属性
        return self.name.split()[-1] # 对 self.name 做拆分取尾
    def giveRaise(self, percent):
        #改变的值需要写进实例的属性就不用return
        self.pay = int(self.pay * (1 + percent)) # 涨薪后截断小数部分转回整数 只能在这里改
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    #使用新的方法
    print(bob.lastName(), sue.lastName())
    #而不是硬编码
    sue.giveRaise(.10)
    print(sue.pay)