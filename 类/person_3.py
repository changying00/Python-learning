"""（添加构造函数默认值）"""
class Person:
    def __init__(self, name, job=None, pay=0):   # 构造方法：接收三个参数，后两个有默认值
        self.name = name      # 把局部变量 name 存入新实例的 __dict__（键 'name'）
        self.job = job        # 同上，键 'job'
        self.pay = pay        # 同上，键 'pay'