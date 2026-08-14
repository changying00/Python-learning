"""
列表的遍历方式 

    a)  基于索引的遍历  
    
        列表 它的 索引 范围为  0 ~ length - 1 、且 支持 通过 索引获取值 

        len(ls) :  获取 列表的 长度 、在 python 语言中 ，获取长度、均使用 len 函数

    b) 基于 值的遍历 
"""
# 定义一个列表 、
ls = [23, 56, 78, 23, 87, 1]

# 基于 索引的遍历方式 
# for i in range(len(ls)):
#     # 获取 列表中的每一个元素 
#     print(ls[i])

for x in ls:
    print(x)