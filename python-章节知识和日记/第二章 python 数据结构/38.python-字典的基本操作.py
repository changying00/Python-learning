"""
字典 的 基本操作 

    a) 添加数据 
        setdefault(key, default) :  当键不存在的时候，才会向字典中添加数据

    b) 修改数据

    c) 删除数据
        pop(key, default=None) :  根据 键删除 数据、并返回 键对应的 值  
        popitem() : 删除 字典中 最后一个 键值对 、并返回一个元组 (不常用)

        clear() :  清空 整个字典 

    d)  查询数据 

        dct[key] :  根据键 获取值 、 键不存在 ，会 抛出错误 
        get(key, default=None) :  获取指定的键、 如果 键不存在，则 返回 默认值 

"""
# 创建一个 空字典 
dct = {}

# 向字典中添加数据(键值对) 
dct["name"] = "张三"  

dct["name"] = "李四"

# 使用 setdefault 方法 添加数据 
dct.setdefault("age", 20)
dct.setdefault("name", "赵六") 

dct["birth"] = "1990"
dct["xxx"] = "123"

# 删除 字典中的年龄 
# age = dct.pop("age") 
# print("被删除的age 值为", age)
# print(dct.popitem())
# dct.clear()

print(dct)

# print(dct["name"])
# # print(dct["gender"])

# print(dct.get("name", "XXX"))
# print(dct.get("gender", "保密"))
