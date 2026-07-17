#字典的创建方式
# print(dict.fromkeys("a2323",1))
# #dict函数(构造器)中的每一组参数就是字典中的一组键值对
# print(dict(name = "dgx",age = 18,性别 = "男"))
#
# #通过python 的内置函数zip压缩俩个序列并创建字典
# items1 = dict(zip("ABCDEF",[1,2,3,4,5,6]))
# print(items1)
# items2 = dict(zip("ABCDEF",range(1,21)))
# print(items2)
# items3 = dict(zip("ABCDEF","212121"))
# print(items3)

# person = {
#     "name":"dgx",
#     "age":23,
#     "height":183,
#     "weight":60,
#     "addr":["河南省商丘市"]
# }
# print(len(person)) #5
# #for循环只是对字典的键进行了遍历
# for i in person:
#     print(i)
# #成员运算
# print("name"in person)
# print("ls"in person)
# person["name"]="db"
# person["age"]=22
# person['tel'] = 212312312312
# person['signature'] = '你的男盆友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
# print(person)
#
# # 循环遍历
# for key in person:
#     print(f'{key}:\t{person[key]}')

person = {
    "name":"dgx",
    "age":23,
    "height":183,
    "weight":60,
    "addr":["河南省商丘市"]
}
# person["name"] = "hx"
# print(person["name"])
#如果删除的键，字典中没有则返回default对应的值
# a = person.pop("name1",1)
# print(a)
# print(person)
#删除字典中最后一个键值对、并返回一个键和值组成的二元组
# print(person.popitem())
# print(person)

# #返回一个None
# print(person.clear())
#
# #删除返回一个空{}
# person.clear()
# print(person)

#查询对应键的值
# a = person["name"]
# print(a)

#返回能查询到键的值，如果没有对应键则返回default设置的值，默认为None
# print(person.get("name"))
#返回None
# print(person.get("name1"))
#返回1
# print(person.get("name"))

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



# 合并 2个 字典
#  **dct 展开 字典 、并将 字典中数据 转成关键字
#  此时 要展开的 字典 它的键 必须 全部是 字符串
# dct3 = dict(**dct, **dct2)
# print(dct3)

# 使用 | 合并 字典
# dct4 = dct | dct2
# print(dct4)