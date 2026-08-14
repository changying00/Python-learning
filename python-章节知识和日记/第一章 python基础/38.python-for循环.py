"""
for 循环 :  主要用来 遍历 可迭代的 对象 

    常见的 可迭代对象 包含  
        1)  range 对象 
        2)  字符串 
        3)  列表
        4)  元组
        5)  集合
        6)  字典

语法:

for var in iterable:
    pass
else:
    pass

- var :  变量名 、由 开发人员自主命名、代表 可迭代对象中的 每一个 数据 
- iterable :  遍历的 可迭代对象

for 循环 也支持 break 和 continue 关键字 来 控制循环 。


"""

# 在 控制台上输出 10 ~ 100 所有 数字 
# x = 10
# while x <= 100:
#     print(x)
#     x += 1

# for x in range(10, 101):
#     print(x)

# 计算 1 + 3 + 5 + 99 的 和 
# x = 1
# s = 0 
# while x < 100:
#     s += x 
#     x += 2

# print(s)

# s = 0
# for x in range(1, 100, 2):
#     s += x 

# print(s)