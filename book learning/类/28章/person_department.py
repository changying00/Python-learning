from  person_10 import Person,Manager
class Department:
    def __init__(self,*args):
        # 把所有参数收进一个列表
        self.members = list(args) #管理一个对象列表

    def addMember(self,person):
        self.members.append(person)

    # 批量操作：每个成员按自己的类型涨薪
    def giveRaises(self,percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        # 多态在这里生效
        for person in self.members:
            print(person)

if __name__=='__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    pat = Manager('Pat Jones', 50000)
    development = Department(bob, sue)  # 把对象嵌入复合中
    development.addMember(pat)
    development.giveRaises(.10)  # 运行内嵌对象的 giveRaise
    development.showAll()     # 运行内嵌对象的 __repr__