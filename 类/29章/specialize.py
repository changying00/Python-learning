class Super:
    def method(self):
        print('in super.method')

    def delegate(self):
        self.action() #期望在子类中定义

#原封不动继承方法
class Inheritor(Super):
    pass

#完全的替代方法
class Replacer(Super):
    def method(self):
        print('in Replacer.method')

#扩展方法行为
class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self) #或者 super().method()
        print('ending Extender.method')

#填上被期望的方法
class Provider(Super):
    def action(self ):
        print('in provider.action')

if __name__ == '__main__':
    # for klass in (Inheritor,Replacer,Extender):
    #     print("\n" + klass.__name__ + '...')
    #     klass().method()
    # print('\nprovider...')
    # x = Provider()
    # x.delegate()
    # x.action()

    print(Inheritor.__dict__)
    print(Inheritor.__doc__)
    print(Inheritor.__bases__)
    print(Inheritor.__mro__)
    print(Inheritor.__name__)
