"""
    断言型函数: 有参数 且返回 bool 值 是一种特殊的 功能型函数

    断言型函数 往往 应用于 数据筛选

    定义一个 过滤 函数、保留 可迭代对象中满足条件的数据、并返回一个 新的列表对象
"""
def filters(iterable,predicate):
    """ 保留可迭代对象中满足条件的数据、返回一个新的列表"""
    return [v for v in iterable if predicate(v)]

# 定义一个字符串 列表
ls  = ["xyz","abc","10","yf","2211"]

#使用filter 函数 过滤并保留 长度为3的数据
print(filters(ls,lambda x: len(x)==3))

#定义一个数字列表
ls2 = [22,2,1,212,212,1213,2131]

#使用filter函数 过滤并保留 列表中所以的偶数
print(filters(ls2,lambda x: x & 1 == 0))