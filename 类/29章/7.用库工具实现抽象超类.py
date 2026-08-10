from abc import ABCMeta, abstractmethod# 从标准库 abc 模块导入工具

class Super(metaclass=ABCMeta):  # 用元类 ABCMeta 创建这个类
    def delegate(self):  # 普通方法：定义流程
        self.action()
    @abstractmethod # 装饰器：把 action 标记为抽象方法
    def action(self):
        pass    # 占位实现，运行时不可用


class Sub(Super):
    pass



class Dub(Super):
    def action(self):
        print("okay")

X = Dub()
X.delegate()
print(Super.__dict__)
print(Dub.__dict__)#'__abstractmethods__': frozenset() 没有了不报错
print(Sub.__dict__)#'__abstractmethods__': frozenset({'action'}) 抽象还含有还会报错