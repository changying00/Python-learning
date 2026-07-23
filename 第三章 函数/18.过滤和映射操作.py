"""
filter(predicate,iterable) : 获取 可迭代对象 中 满足条件的数据、并返回一个 filter 可迭代对象

map(function,*iterable): 将 多个可迭代对象 同一个位置的元素进行 映射、并返回 一个map 可迭代对象
"""
ls = [23,1,3,4,6,3,233,4,43]

#使用filter 函数 保留 所有的奇数
ret = filter(lambda x: x & 1 ,ls)

print(ret,list(ret))


