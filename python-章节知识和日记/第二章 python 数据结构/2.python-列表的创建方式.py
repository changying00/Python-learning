"""


列表 list 是一个 非常重要的  用来存储多个数据的容器 

    存储的数据 是 有序、且 可重复的 ~~~

列表的创建方式 

    a) 字面量 定义 :  使用 中括号 存储多个数据、且多个数据之间使用 逗号分隔

    b) list工厂函数 :  将一个 可迭代对象 、通过 list 函数 转成 列表对象 

        可迭代对象 : 字符串、列表、集合、字典、元组、 range 对象

    c) 列表 生成推导式

        [ exp for var in iterable [for var in iterable ...] [if condition] ]

    最外层 的中括号 是 列表生成推导式 的 语法 结构 
    里面的 中括号 代码 括起来的 结构 可有可无 

    对一个可迭代对象 进行遍历 、保留 满足条件的数据 、并 映射为 指定的数据 

"""

# 创建一个 空列表 
ls = []

print(ls, type(ls), list())

# 创建一个 包含 指定 内容的列表 
ls2 = [1, 2, 3, 10, 4, 5, 1]

print(ls2)

ls3 = [1, 2, 3, 10, 4, 5, 1]

print(ls3)

print(ls2 == ls3,  ls2 is ls3)

# 将一个字符串 转成列表 
ls4 = list("hello")
print(ls4)

# 将一个数字序列转成列表 
ls5 = list(range(10, 20))
print(ls5)

# 将一个 元组转成列表 
ls6 = list((1, 2, 3, 1, 2))
print(ls6)

# 将一个集合转成列表 
ls7 = list({23, 56, 98, 1})
print(ls7)

# 将一个字典 转成列表 
dct = {"name": "张三", "age": 20}
# 将 字典转成 列表 、只 保留 字典中的 键组成的 列表 
ls8 = list(dct)
print(ls8)


# 使用 列表生成推导式 构建 一个 包含 1 ~ 10 的列表 、且 只保留 能被 3 或者 5 整除的数、最后将 数字在原值的基础上 扩大10倍
ls9  =  [x * 10 for x in range(1, 11) if x % 3 == 0 or x % 5 == 0]

print(ls9)

# 使用 列表生成推导式  生成一个列表 、且列表中 包含  1, 2, 3, ... 10 的所有数字的 平方 

ls10 = [x ** 2 for x in range(1, 11)]

print(ls10)

# 使用 列表生成推导式 快速 构建一个 由 1, 2, 3 组成的所有 三位数 
ls11 = [x*100 + 10*y + z for x in range(1, 4) for y in range(1, 4) for z in range(1, 4) if x != y and y !=z and x !=z ]

print(ls11)
