"""
字典 支持的运算符 :

    a)  位运算符  |  

    b)  成员运算符  
            in  /  not in 
        判断 指定的 键 是否在 字典中 存在 

    c)  关系运算符 
         ==    用来比较 2个 字典 内容是否相同 
         !=

"""

# # 定义 2个字典 
# dct = {"a": 1, "b": 2, "c": 3,  1: 2}

# dct2 = {"x": "10", "y": "20"}

# # 判断 x 是否是 dct2 的成员 
# print("10" in dct2)


# 合并 2个 字典 
#  **dct 展开 字典 、并将 字典中数据 转成关键字 
#  此时 要展开的 字典 它的键 必须 全部是 字符串 
# dct3 = dict(**dct, **dct2)
# print(dct3)

# 使用 | 合并 字典 
# dct4 = dct | dct2 
# print(dct4)

# # 使用 update 合并字典 
# dct.update(dct2)

# print(dct)

# 定义 2个字典 
# dct1 = {"x": 1, "y": 2}

# dct2 = {"y": 2, "x": 1}

# print(dct1 == dct2)

ls = [
    {"name": "张三", "age": 20, "score": 80},
    {"name": "李四", "age": 20, "score": 67},
    {"name": "王五", "age": 20, "score": 83},
    {"name": "赵六", "age": 22, "score": 81},
    {"name": "路奇", "age": 10, "score": 87},
    {"name": "XXX", "age": 30, "score": 90},
]

# 要求 对列表 进行排序 、按照 年龄升序排列 、如果 年龄相同、 则 按照 成绩降序排列 
ls.sort(key=lambda d: (d.get("age"),  -d.get("score")))

print(ls)
