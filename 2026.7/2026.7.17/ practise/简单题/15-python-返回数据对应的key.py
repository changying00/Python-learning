#【字典】定义一个字典 和一个 数据，如果该 数据 存在于字典中，返回对应的 key 列表（可能有多个 key 对应相同的 数据

# #定义一个字典
# dic1  = {"a":1,"b":2,"c":3,"d":1,"e":2,"f":3,"g":4,"h":2}
# #定义一个数据
# num = 2
# #定义一个列表用于存储相同的键
# lis1= []
# #定义一个循环
# for key,value in dic1.items():
#     #如果对应的value == 2
#     if value == num:
#         #把对应的键增加到列表种
#         lis1.append(key)
# print(lis1)

#列表推导式
dic1 = {"a":1,"b":2,"c":3,"d":1,"e":2,"f":3,"g":4,"h":2}
num = 2
lis1 = [
    key
    for key,value in dic1.items()
    if value == num
]
print(lis1)
