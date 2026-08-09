"""添加属性初始化"""
class Person:
    def __init__(self, name, job, pay):     # 构造函数接收三个参数
        self.name = name                     # 创建时填好字段
        self.job = job                       # self 是新建的实例对象
        self.pay = pay