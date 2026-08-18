class SharedData:
    attr = 16 #顶层赋值，属于类的属性，对创建的实例共享

#创建俩个实例
x = SharedData()
y = SharedData()
#他们共享attr 的数据，通过继承查找
print(x.attr,y.attr)

#外部修改类的属性
SharedData.attr = 32
print(x.attr,y.attr,SharedData.attr)

#修改实例的属性，如果没有则直接在实例的命名空间创建，通过__dict__ 可以查看
x.attr = 64
print(x.__dict__)
#由于继承查找机制，当你x.attr的时候，首先先查找实例x的空间有没有 attr 的值，如果有就返回这个，y.attr自身没有，则继承类ShareData的属性attr
print(x.attr,y.attr,SharedData.attr)
