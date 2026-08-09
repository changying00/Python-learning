from  person_10 import  Person  # Example 28-10 的 Person
#注意这不是继承 Person
class Manager:
    def __init__(self,name,pay):
        self.Person = Person(name,"mgr",pay)  # 嵌入一个 Person 对象

    def giveRaise(self,percent,bonus = .10):
        self.Person.giveRaise(percent + bonus)

    def __getattr__(self,attr):
        return getattr(self.Person,attr)

    def __repr__(self):
        return str(self.Person) # 必须重新重载（见后文）

if __name__=="__main__":
    pat = Manager('Pat Jones',50000)
    pat.giveRaise(.10)
    print(pat.lastName())
    print(pat)