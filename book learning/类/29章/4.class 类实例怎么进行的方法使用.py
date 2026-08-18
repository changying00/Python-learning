class NextClass: #定义类
    def printer(self,text):#定义一个方法
        self.message = text #修改实例
        # print(self.message)  #访问实例
        #改成return 返回
        return self.message
x = NextClass() #创建一个实例
#第一种通过实例本身继承查找
print(x.printer("instance call")) #调用它的方法
#上面实例被修改了，我们直接找实例的属性名进行
print(x.message)
#第二种方法 通过类本身调用
print(NextClass.printer(x,"class call")) #调用方法实例再次被修改
print(x.message)
#看到实例和方法是否绑定 <bound method NextClass.printer of <__main__.NextClass object at 0x000002683E0751C0>>
print(x.printer)
print(NextClass.__mro__)

