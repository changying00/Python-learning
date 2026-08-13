"""
浅拷贝：创建新的外层对象，但内部对象仍共享原对象的引用。

深拷贝：创建新的外层对象，并递归复制内部需要复制的对象，使复制后的对象结构与原对象相互独立。


浅克隆 ： 将一个 要 克隆的 对象 它的数据 不可变类型 进行 值拷贝、可变类型 进行 引用地址拷贝
copy.copy(不可变对象)
→ 通常直接复用原对象

copy.copy(可变容器)
→ 创建新的外层容器
深克隆 ： 将一个 要 克隆的 对象 它的数据 不可变类型 进行 值拷贝、可变类型 进行 递归的 浅克隆
"""
import copy
#
# class Book:
#
#     def __init__(self,name):
#         self.name = name
#
# class Human:
#
#     def __init__(self,name,book):
#         self.name = name
#         self.book = book
#
# #创建一个 人类对象 、该人类对象book属性 拥有一本书，然后这个地址是可变类型，应该进行地址拷贝
# p = Human("张三",Book("平凡的世界"))
# print(p.__dict__)
# print(p.book.__dict__)
# p1 = copy.copy(p)
# p.name = "李四"
# p.book = "天龙八部"
# print(p.book)
# print(p1.book)
# print(p1.name)
# print(p.name)
# print(p.book.name)
ls = [[1,2],[3,4,5]]
new_ls =  copy.copy(ls)
print(ls[0] is new_ls[0])

ls2 =  [1,2,3,4]
new_ls2 = copy.copy(ls2)
print(ls2[0] is new_ls2[0])

#看整个对象不相同，但是内部相同，修改了，对应的拷贝也修改

