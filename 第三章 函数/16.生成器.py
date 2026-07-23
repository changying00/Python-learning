"""
生成器 generator : 是一种 特殊的迭代器、拥有迭代器的所有的特点。

生成器的主要作用 :

        a) 可以节约内存

        b) 可以表示无穷数据

生成器的创建方式

        a) 元组生成推导式

        b) 函数 + yield

如果 函数 中使用 yield 关键字返回数据、那么这个函数、被称为生成器函数

生成器函数 调用后 返回一个 生成器对象、且 此时 函数中的代码 不会执行。

当调用 next 函数 获取数据的时候 、会执行 函数中的代码、通过yield 返回数据

且程序会 自动 进入挂起状态、等待下一次 调用next
"""
# 使用 元组生成推导式 构建一个生成器
# gen = (x ** 2 for x in range(10))
#
# print(next(gen))
# #上面取出来一个过后，下面从1开始
# for x in gen:
#     print(x)

def generator_key():
    #唯一标识
    identify = 0
    while True:
        # print("Hello",identify)
        #将唯一标识 值增加1
        identify += 1
        #使用yield 返回 identify
        yield identify
        # print("world")

#调用 函数
gen = generator_key()
print(next(gen))
ls1 = []
while True:
   ls1.append(next(gen))
   print(ls1)
