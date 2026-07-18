#【字典】给定字典 d = {'a': 1, 'b': 2, 'c': 3}，删除所有 value 小于 2 的键值对。
dic1 = {'a':1, 'b':2, 'c':3}
# new_dic = {}
# for key,value in dic1.items():
#     if value >= 2:
#         new_dic[key] = value
# print(new_dic)

#列表推导式
# dic1 = {'a':1, 'b':2, 'c':3}
#
# dic2 = {
#     key:value
#     for key,value in dic1.items()
#     if value >= 2
# }
#
# print(dic2)
#第三种方法，如果不加list ，dic1.keys()是个动态的，在执行循环会报错，加上list变成静态
for key in list(dic1.keys()):
    if dic1[key] < 2:
        dic1.pop(key)
print(dic1)