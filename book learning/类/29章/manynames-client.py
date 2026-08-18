import manynames

X = 66
print(X)           #66；这是全局变量

print(manynames.X) #11:导入后全局变量变成属性
manynames.f()      #11:manynames的X，不是这里的
manynames.g()      #22:另一个文件函数里的局部


print(manynames.C.X) #33:另一个模块里的类属性

I = manynames.C()
print(I.X)           #33:这里仍然来自类
I.m()
print(I.X)           # 55:现在来自实例！
