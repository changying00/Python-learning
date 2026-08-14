"""
字典 :  是一个用来存储多值的容器、它的每一个数据 由 键和值 两部分组成 

在 编程中 、字典 通常 可以用来 描述一个 对象的信息 、 例如 某个人 (姓名、年龄、性别、...)

字典 底层 采用 散列表 + 链表 结构 进行数据存储的 。 

字典 键 的特点 :  不可重复、且 键 必须是 可 hash 的 、只能 是 不可变类型 、例如 数字、字符串、bool 、元组 , None 


字典 dict 的创建方式 :

    1. 字面量 

    2. dict 工厂函数

        a)  支持 传入一个 二维 可迭代对象 、且 可迭代对象中的 可迭代对象长度 必须是 2

            [ [1, 2], [3, 4], [5, 6] ]

            [ ("name", "张三"), ("age", 20),  ("sex", "男") ]

        b)  支持传入 关键字 参数 、直接 转成 字典 

            dct5 = dict(a=1, b=2, c=3)

        c)  可以 将 字典 转成 字典 

            dct6 = dict(**dct5, **dct4)
            print(dct6)

    3. 字典生成推导式 

        语法  { exp1:exp2  for var in iterable [for var in iterable ...] [if condition] }

    4. 静态方法 fromkeys 

        dict.fromkeys(iterable, fillvalue=None):
            将 可迭代对象中的数据 作为 键 , 并给 键 填充值位  fillvalue 

"""
# 创建一个 空字典 
dct = {}
print(dct, type(dct))

# 创建一个 包含数据的 字典、键和值 使用 : 分隔、 多个值 之间使用 逗号分隔
dct2 = {"name": "张三", "age": 20, "gender": "男"}
print(dct2)

# 使用 dict 工厂函数 构建字典 
# 
dct3 = dict([ [1, 2], [3, 4], [5, 6] ])
print(dct3)

dct4 = dict([ ("name", "张三"), ("age", 20),  ("sex", "男") ])
print(dct4)

# 将 关键字参数 转成 字典 
dct5 = dict(a=1, b=2, c=3)
print(dct5)

dct6 = dict(**dct5, **dct4)
print(dct6)

# 定义一个 字典 、 将 键和值 进行互换 
dct7 = { v:k for k, v in dct4.items() }
print(dct7)

# 使用 静态方法 构建 一个字典 、要求传入一个 可迭代对象
dct8 = dict.fromkeys("abc", 1)

print(dct8)