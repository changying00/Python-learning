from openpyxl.workbook.defined_name import DefinedName


class FirstClass:
    def setdata(self,value):
        self.data = value

    def display(self):
        print(self.data)

#
# if __name__ == '__main__':
#     x = FirstClass()
#     y = FirstClass()
#     #
#     x.setdata("coding")
#     y.setdata(3.1415926)
#
#     x.display()
#     y.display()
#     x.data  = "dgx"
#
#     x.display()
    
class SecondeClass(FirstClass): #继承setdata属性
    def display(self):
        print(f"Current value = '{self.data}'") #替换父类FirstClass里的display属性 在树的更低位置重新定义以替换属性"的行为称为重载（overloading）
       

# if __name__ == "__main__":
#     z = SecondeClass()
#     z.setdata("hx")# 在 FirstClass 中找到 setdata
#     z.display()      # 在 SecondClass 中找到被覆盖的方法
 #Current value = "hx"


class ThirdClass(SecondeClass):
    # 在 "ThirdClass(value)" 时运行
    def __init__(self,value):
        self.data = value
    def __add__(self,other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return f'[ThirdClass:{self.data}]'
    def mul(self,other):
        self.data *= other

if __name__ == "__main__":
    a = ThirdClass(3)
    a.display()
    b = a + 3
    b.display()
   #__str__:返回显示字符串
    print(b)
    #mul 原地修改实例
    a.mul(4)
    print(a)
#__init__`（构造时初始化）、`__add__`（`+` 表达式）、`__str__`（打印）。
# 注意它们的共同点——**都是普通属性**，与其他方法无异，只是名字碰巧被语言"约定"了。
#以为 __init__ 是"分配内存"——不是，那是 __new__ 的活
 # 空的命名空间对象
# class rec: pass
#
#
# if __name__ == "__main__":
#     rec.name  = "DGX"
#     rec.age  = 40
#     print(rec.name)
#     print(rec.age)
#
#     x = rec()
#     y = rec()
#     print(x.name,y.name)
#     """如果我们真的给某个实例赋值一个属性，它只会在那个对象中创建（或改变）属性，
#     而不会影响其他对象——关键在于：属性引用会触发继承搜索，但属性赋值只影响被赋值的对象本身。
#     在这里，这意味着 x 得到了自己的 name，而 y 仍然继承挂在类上的 name："""
#     x.name = "hx"
#     print(x.name,y.name,rec.name)
# #读取走继承，写入不传播*
# # class A:
# #     name = 20
# # a1 = A()
# # b1 = A()
# # print(a1.name,b1.name)
#
# print(list(key for key in rec.__dict__ if not key.startswith('__')))
# print(list(x.__dict__))
# print(list(y.__dict__))
#
# print(x.name, x.__dict__['name'])
# print(x.age)

#属性记法获取-前提存在于被查的那个对象上：属性标记法会触发继承搜索，
#而字典索引只查单个对象
# print(x.__dict__['age'])  #会报错因为索引字典不能继承，x没有age属性
# print(x.__dict__) #只有 name 属性和对应的值

#而 dir 内建函数会收集继承来的名字：
# print([attr for attr in dir(x) if attr[:2] != '__'])
# #方便属性获取时的继承搜索，每个实例都有一个指向其类的链接
# print(x.__class__)
#
# #类还有一个__bases__属性 他是一个元组，包含对类超类对象的引用
# print(rec.__bases__)# 类到超类的链接
# #(<class 'object'>,)
# def uppername(obj):
#     return obj.name.upper()
#
# print(uppername(x),uppername(rec))
# rec.method = uppername
# print(x.method())
# print(rec.method(x) )
# #俩种调用方法 同一个函数对象，两种调用姿势——绑定与否，只看访问它时经过了谁。
# print(dir(rec))