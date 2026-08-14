"""
列表的遍历方式 

    a)  基于 索引的遍历方法 、 配合  len 函数 

    for i in range(len(ls)):
        print(ls[i])

    
    b)  基于 值的遍历方式 

    for val in ls:
        print(val)


    c)  基于 索引 和 值的 遍历方式 、配合 enumerate 函数 

    enumerate 枚举函数 它的作用 就是 将 一个 可迭代对象中的 数据 转成 元组 、且 元组 中 第一个元素 代表 索引值 、第二个代表 元素 。

    for index, value in enumerate(ls):
        print(index, value)

"""

# 定义一个列表 
ls = [23, 6, 5, 65, 54, 8, 23, 87,1, 65]
# 将 列表 对象 通过 enumerate 转成 枚举对象 
#  enumerate 对象 也是一个 可迭代对象 
# enum_obj = enumerate(ls)
# print(list(enum_obj))

# for index, value in enumerate(ls):
#     print(index, value)
# 使用 列表 生成 推导式 获取 一个列表的 偶数索引 对应的 值 
new_ls = [value for index, value in enumerate(ls) if index & 1 == 0 and value & 1 ]
print(new_ls)