"""
元组 支持的遍历方式  

    a) 基于 索引的遍历 、配合 len 函数 

    b) 基于 值的 遍历 

    c) 基于 索引和值的遍历、 配合 enumerate 函数 

"""

tp = (1, 34, 65, 78, 0)

# 使用 索引遍历 元组 
for x in range(len(tp)):
    print(tp[x])

print("=" * 100)

# 使用 值遍历元组 
for v in tp:
    print(v)

print("=" * 100)

# 使用 索引 和值 的遍历方式 
for i, v in enumerate(tp):

    print(i,  v)