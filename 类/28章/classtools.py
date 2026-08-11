#"Assorted class utilities and tools"   # 杂项类工具
class AttrDisplay:
    """
       提供一个可继承的显示重载方法：显示实例的类名，以及
       实例自身存储的每个属性的 name=value 对（不含从类继承
       来的属性）。可以混入（mixin）任何类，对任何实例都有效。
       """
    def gatherAttrs(self):
        attes = []
        for key in sorted(self.__dict__): # 按键名排序，逐个取属性
            attes.append(f'{key}={getattr(self, key)}')# 用 getattr 取属性值
        return ','.join(attes) #连接成 'attr1=0, attr2=1'
    def __repr__(self):
        # 动态取真实类名
        return f'{self.__class__.__name__}({self.gatherAttrs()})'

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0   # 类属性：所有实例共享
        def __init__(self):
            self.attr1 =TopTest.count # 实例属性
            self.attr2 =TopTest.count +1
            TopTest.count += 2  # 每次创建都递增
    class SubTest(TopTest):
        pass           # 什么也不做，仅继承
    # X,Y,Z=  TopTest(), SubTest(),SubTest()    # 创建两个实例
    # print(X)# 显示全部实例属性
    # print(Y) # 显示最低层的类名
    # print(Z)
    # print(X.__dict__)
    # result = [a for a in dir(X) if not a.startswith('__')]
    # print(result)
    # print(SubTest.__bases__)
    # print(TopTest.__name__)
    # # print(X.__name__)
    # print(X.__class__)
    print(dir(TopTest))
    print(dir(AttrDisplay))