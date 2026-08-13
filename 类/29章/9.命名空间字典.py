class Super:
    def hello(self):
        self.data1 = "hack"

class Sub(Super):
    data4 = 123
    def hola(self):
        self.data2 = "code"

X = Sub()
print(X.__dict__) #此时实例命名空间字典为空

print(X.__class__) #实例的类

print(Sub.__bases__) #类的超类

print(Super.__bases__) #顶层之上隐式的，顶层类都是object

Y = Sub()
X.hello()
print(X.__dict__) #当实例通过继承搜索到方法hello(),使用之后，会给自己的命名空间字典里面添加一个属性
X.hola()
print(X.__dict__)  #这时候又又使用一个方法给自身的命名空间赋值

print(list(Sub.__dict__.keys())) #这是Sub类命名空间字典存的键名

print(list(Super.__dict__.keys()))#这是Super类命名空间存的键名
print(list(Super.__dict__))#这俩种方式为啥结果一样
print(Y.__dict__)

print(X.data1, X.__dict__['data1'])#俩种获取的方式 限定或通过键索引

X.data3 = 'docs'
print(X.__dict__)
X.__dict__['data3'] = 'apps' #通过索引键值
print(X.data4) #通过继承查找，找到类里面的属性
print(X.__dict__)
print(dir(X))