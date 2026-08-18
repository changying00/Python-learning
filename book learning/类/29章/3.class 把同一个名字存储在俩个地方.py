class MixedNames: #定义类
    data = 'text'  # 赋类属性——类对象的数据
    # 赋方法名——类对象的函数属性
    def __init__(self,value):
        self.data  = value  # 赋实例属性——每个实例各自的 data
#方法里面没有return 返回值默认返回None
    def display(self):
        return(self.data,MixedNames.data)#实例属性，和类属性

x  = MixedNames(1)  # 创建两个实例对象
y  = MixedNames(2)   # 每个都有各自的 data

print(x.display())   # self.data 不同，MixedNames.data 相同
print(y.display()) 

print(x.__class__,y.__class__)
