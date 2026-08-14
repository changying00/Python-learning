"""
元组 tuple :   它的底层采用 线性表 进行数据存储、 它存储的元素 有序 且 可重复的 、元组 是 不可变的 

元组 在 定义的时候 使用  () 语法 定义 、且 性能 比 列表 更高 ~~~  

元组的 定义方式  

    a)  字面量 

    b)  tuple 工厂函数 

        tuple 工厂函数 可以将 任意 的 可迭代对象 转成 元组 

"""

# 创建一个 空元组 
tp = ()
print(tp, type(tp))

# 创建一个长度 为 1 的元组 、此时 必须 添加一个 逗号 
tp2 = (1, )
print(tp2, type(tp2))

# 创建一个 长度 超过 1 的元组 
tp3 = (1, 2, 3)
print(tp3, type(tp3))

# 在 使用 字面量 定义 元组的时候 、如果 元组的 数据个数 大于 0 、还可以 省略 小括号 
#  不建议 省略 小括号 ~~~ 
tp4 = 10, 30
print(tp4, type(tp4))

a = 10 
b = 20 
# 实现  2个数字的交换 
# b, a 两个变量的值 构成了 一个元组 、采用 解包的方式 将 元组中的数据 分别 赋值给 a, b 
a, b = b, a


# 定义一个 列表 
ls = ["x", "y", "z"]

print(tuple(ls))

print(tuple("abc"))

# python 中 也存在 元组生成推导式 
#  (exp for var in iterable [for var in iterable ...] [if condition])
# 使用 元组生成推导式 、生成一个  1 ~ 100 的数字 对象 

obj = (x for x in range(1, 101))

print(obj, type(obj))

print(tuple(obj))



