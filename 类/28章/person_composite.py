from  person_10 import  Person  # Example 28-10 的 Person
#注意这不是继承 Person
class Manager:
    def __init__(self,name,pay):
        #嵌入：self.person就是一个Person实例
        self.person = Person(name,"mgr",pay)  # 嵌入一个 Person 对象

    def giveRaise(self,percent,bonus = .10):
        #拦截后转发给嵌入对象
        self.person.giveRaise(percent + bonus)

    def __getattr__(self,attr):
        #其他属性一律委托给嵌入的对象
        return getattr(self.person,attr)

    def __repr__(self):
        # 显示也转发（内置操作不会触发 __getattr__）
        return str(self.person) # 必须重新重载（见后文）

if __name__=="__main__":
    pat = Manager('Pat Jones',50000)
    pat.giveRaise(.10)
    print(pat.lastName())
    print(pat)