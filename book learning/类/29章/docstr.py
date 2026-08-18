"I am: docstr.__doc__"                    # 模块级文档字符串
def func(args):
    "I am: docstr.func.__doc__"           # 函数文档字符串
    pass
class Klass:
    "I am: Klass.__doc__ or docstr.Klass.__doc__ or self.__doc__"   # 类文档字符串                                 # 类文档字符串
    def method(self):
        "I am: Klass.method.__doc__ or self.method.__doc__"
        # 方法文档字符串
        print(self.__doc__)
        print(self.method.__doc__)
if __name__ == '__main__':
    i = Klass()
    print(i.__doc__)