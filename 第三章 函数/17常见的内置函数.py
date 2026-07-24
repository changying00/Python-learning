"""
__name__ :获取当前模块名、__main__代表 当前模块是顶层模块
直接 运行的模块 叫顶层模块、顶层模块 名字叫__main__

__doc__ :获取 当前模块的文档信息
__file__ :获取 当前模块 所在的磁盘路径
"""
print(globals())
"""
- abs(x) : 获取一个数字的绝对值 

- all(iterable) :  可迭代对象中的数据 是否 均为 真
- any(iterable) :  可迭代对象中的数据 是否 有 真 

- pow(x, y) :  获取 x 的 y 次幂

- round(x, n) :  四舍六入五成双

"""
# print(abs(-10.2), abs(10.2))

# print(all([1, 2, 3, 4, 5]))
# print(all((1, 2, 3, 0)))

# print(any([0, "", [], (), {}]))

# print(pow(2.5, 3))    0, 3, 4, 7, 8 （进）   1, 2, 5,6, 9 (舍)

# print(round(5.205, 2))  # 5.20   ❌     --- 0 进
# print(round(5.215, 2))  # 5.22   ❌     --- 1

# print(round(5.225, 2))  # 5.22          --- 2
# print(round(5.235, 2))  # 5.24          --- 3 进

# print(round(5.245, 2))  # 5.24   ❌    --- 4  进
# print(round(5.255, 2))  # 5.26   ❌    --- 5

# print(round(5.265, 2))  # 5.26          --- 6
# print(round(5.275, 2))  # 5.28          --- 7 进

# print(round(5.285, 2))  # 5.28   ❌     --- 8 进
# print(round(5.295, 2))  # 5.3    ❌     --- 9

# # 获取 指定 字符的 ascii 值 、超出 ascii范围的字符 以 unicode 编码 表示
# print(ascii("abc123"))
# print(ascii("中国"), ord("中"))     # \u4e2d  ===> 20013


# string = b"\u4e2d\u56fd"

# print(string.decode("unicode-escape"))

# # 获取 两个数字的  商 和余数
# print(divmod(3, 2))

# print(hash("abc"),  hash("abc"))

# set = {"xyz", "abc", "123"}

# print(set)

# isinstance(obj, type|tuple) :  判断 对象 是否是 某种类型

# print (type(1)  == int)

# print(isinstance(1, (int, float)))

#
# ls = [3,  6, 98, 12, 76]
# ls = [
#     {"name": "张三", "age": 60},
#     {"name": "李四", "age": 70},
#     {"name": "王五", "age": 50},
# ]

# print(max(ls, key=lambda d: d.get("age")))
# print(min(ls, key=lambda d: d.get("age")))

# globals()  :  获取 当前上下文 定义的所有 全局变量 组成的 字典

a = 10
b = 20


def test(a):
    c = 30
    print(globals())
    # 获取 当前上下文中 定义的所有 局部变量
    print("=============================================")
    print(locals())


test(a)
