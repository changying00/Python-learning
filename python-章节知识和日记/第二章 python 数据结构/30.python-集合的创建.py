"""
集合 set 的创建方法 

    a) 字面量 

    b) set 工厂函数 
        可以 将 任意 可迭代对象 转成集合 

    c) 集合生成推导式  

        语法 {exp  for var in iterable [for var in iterable ...] [if condition]}


sorted 是 一个内置函数、可以对任意的可迭代对象进行排序 

    sorted(iterable, *, reverse=False, key=None)


"""

# 创建一个包含指定内容的集合 
s1 = {1} 
print(s1, type(s1))

s2 = {1, 2, 3, 1, 2}
print(s2, type(s2))

s3 = {"xyz", "abc", "123", "ttt", "fff"}
print(s3, type(s3))

# 已知 一个列表 、要求 对 列表中的元素 去重 、并返回一个新列表、且元素 保留原有的顺序。

# 使用 set 工厂函数 
ls = [3, 65, 87, 123, 65, 1, 3]
# 将 列表转成 集合 
s4 = set(ls)
print(s4, type(s4)) 
# 去重后 保持 原有顺序 
print(sorted(s4, key=lambda d: ls.index(d)))

# 创建一个 空集合 
s5 = set()
print(s5, type(s5))

# 使用 集合生成推导式 构建一个 包含 1 ~ 10 的元素 
s6 = {x for x in range(1, 11)}

print(s6)



