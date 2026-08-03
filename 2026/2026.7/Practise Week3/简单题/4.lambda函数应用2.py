"""
 【lambda】 定义一个 each函数、负责遍历 可迭代对象的 所有数据、并让该函数具备 消费 元素和索引 的能力。
a. 使用 each 函数完成 打印 列表 中所有 元素的索引

b. 使用 each 函数完成 打印 列表中 所有的元素

"""
#定义一个函数each，负责遍历可以迭代对象的所有数据
def each(target,condition):
    #定义一个名为ls1的空列表
    ls1 = []
    for item ,value in enumerate(target):
         condition(item,value)
#定义一个列表ls
ls = [1,2,3,4,5,65,2,34,343,41,41,4,12,41,42]
#获取元素的索引
print("打印索引:")
each(ls, lambda index, item: print(index))
print("打印值:")
each(ls, lambda index, item: print(item))
