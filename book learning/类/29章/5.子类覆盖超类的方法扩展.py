# class Super:
#     def method(self):
#         print("in Super.method")
#
#
# class Sub(Super):
#     #覆盖方法
#     def method(self):
#         print("starting Sub.method")
#         Super.method(self) #运行默认的动作
#         print("ending Sub.method")
# x = Super()  # 创建 Super 实例
# print(x.method())   # 创建 Super 实例
#
# y = Sub()# 创建 Sub 实例
# print(y.method())   # 运行 Sub.method，内部调用 Super.method


class Super:
    def __init__(self,x):
        print('default code')

class Sub(Super):
    def __init__(self,x,y):
       # 这种隐式写法super().__init__(x)等于下面的写法
        Super.__init__(self,x)  # 运行超类的 __init__
        print('custom code')  # 做我自己额外的初始化动作
I = Sub(1,2)
