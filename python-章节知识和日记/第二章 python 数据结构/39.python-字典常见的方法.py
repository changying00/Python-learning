"""
字典 常见的方法 

    - setdefault(key, default) :  当键不存在的时候，设置默认值

    - pop(key, default?) :  根据键删除数据、键不存在，会报错、可以设置 默认值  

    - clear() : 清空集合  

    - get(key, default=None) : 根据键 获取值 、如果键不存在、返回 默认值 


    - copy() :  采用 浅克隆技术 克隆一个 字典 

    - update(dct) :  合并 一个字典 到 指定的字典中 

    - keys() :  获取 字典 中所有的 键 组成的 可迭代容器 
    - values() : 获取 字典中 所有的 值 组成的 可迭代容器 
    - items() : 获取字典中 所有的 键值对 组成的 可迭代容器

字典 常见的遍历方式  

    -  键遍历 

        字典 是 可迭代对象、 支持 直接 使用 for ... in 遍历 、等价于 调用 了 keys()

    -  值遍历 

        值遍历 无法 通过 值 获取 键 

    -  键值对遍历 (最常用)

"""

dct1 = {"name": "张三", "age": 20}

# dct2 = {"name": "李四", "gender": "女"}

# # 合并 2个字典 到 dct1 中 
# dct1.update(dct2)
# print(dct1)

# print(dct1.keys())

# print(dct1.values())
# print(dct1.items())

for key in dct1:
    print(key, dct1.get(key))

print("=" * 100)

for val in dct1.values():
    print(val)

print("=" * 100)

for key, value in dct1.items():
    print(key, value)