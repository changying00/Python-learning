# class Super:
#     def delegate(self):
#         self.action()
#
#     def action(self):
#         assert False,'action must be defined!' #若被调用则报错
#
# x = Super()
# x.delegate()


class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')
# X = Super()
# X.delegate()

#对于子类的实例，除非子类提供了期望的方法来替换超类中的默认版本，否则我们仍然会得到异常：
# class Sub(Super):pass
# X = Sub()
# X.delegate()

class Sub(Super):
    def action(self):
        print("okay")
X = Sub()
X.delegate()
