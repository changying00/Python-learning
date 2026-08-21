"""
什么是 可迭代对象（Iterable）：可以使用 for 循环遍历的对象、
    常见的可迭代对象有
        字符串、列表、元组、集合、字典、range对象、enumerate对象、zip对象

迭代器（Iterator）:

    是一种特殊的可迭代对象、惰性取值

    迭代器 不能使用 len 获取长度、也不支持 索引取值

    迭代器 使用 next 函数获取数据、且 一次 只能 获得1 个数据。当获取 最后一个数据后、再次调用 next 会抛出一个Stopiteration错误
获取 迭代器的方式：

    iter(iterable):将 一个 可迭代对象 转成迭代器。
"""
ls  = [1,2,3,4,5]

it =  iter(ls)
# print(list(it))
print(list(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# for x in it: #迭代器只能遍历一次
#     print(x)
# print(50 * "*")
# for i in  it:
#     print(i)

