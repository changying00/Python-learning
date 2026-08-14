"""
集合 的基本操作 :

    1.  添加数据 
        add(x) :  向集合中添加元素 

    2.  删除数据 

        remove(val) : 删除指定的成员(数据)、 如果 val 不存在，则抛出错误 ~
        discard(val) : 删除指定的成员、 不会报错。
        pop() : 随机删除集合中 一个成员 
        clear() :  清空集合 

常见方法 :
    - copy() :  采用 浅克隆技术 复制一个集合 

并集
    - union(set) :  合并 2 个集合中所有的数据、 并 返回 合并的 新集合 
    - update(set):  合并 2 个集合中所有的数据、将 集合 合并到 第一个 集合中 

交集
    - intersection(set) :  计算 2个集合的交集、并将结果 做成一个 新的集合 
    - intersection_update(set) : 计算 2个集合的交集、并将结果 放到 第一个集合中

差集: 
    - difference(set) :  计算 2个集合的差集、 返回新的集合
    - difference_update(set): 计算 2个集合的差集、并将结果 放到 第一个集合中

补集:
    - symmetric_difference(set) :  计算 2个集合的补集
    - symmetric_difference_update(set) : 计算 2个集合的补集

 其它方法的:
    - issuperset(set) :  判断 当前 集合 是否是 set 的 超集
    - issubset(set) : 判断 当前 集合 是否是 set 的 子集
    - isdisjoint(set) :  判断 两个 集合 是否是 不相交的  



"""

# s1 = {"abc", "123", "xyz"}
# s2 = {"abc", "10", "30", "xyz"}

s1 = {"abc1", "1232", "xyz1"}
s2 = {"abc", "xyz", "123"}

print(s1.issuperset(s2))
print(s2.issubset(s1))
print(s1.isdisjoint(s2))

# print(s1.union(s2))
# print(s1)

# s1.update(s2)
# print(s1)

# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))

# 创建一个 空集合 
# s = set()

# # 向集合中添加数据 
# s.add(10)
# s.add("xyz")
# s.add("abc")
# s.add(10)

# print(s)

# # 根据 值删除 集合中的成员 
# # s.discard("xyz")
# # s.discard("xyz")
# s.pop()

# print(s)

# s.clear()