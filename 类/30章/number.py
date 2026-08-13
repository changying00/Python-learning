#第一种类生成的实例 与 数字 做减法
class Number:
    def __init__(self,start):#在Number(start)时使用
        self.data = start    #保存传入的起始值

    def __sub__(self, other): #在实例 - other时调用
        return Number(self.data - other)     #结果是该类的全新实例，这样类的实例 只能与 数字做 减法

#第二种类生成的实例 与 实例 做减法
class Number1:
    def __init__(self,start):
        self.data = start

    def __sub__(self, other):
        return Number1(self.data - other.data)  #other.data 一改 就变成 类的实例可以属性data 做减法
        #也可以把Number1 改成 Number 这样能控制哪个类的实例