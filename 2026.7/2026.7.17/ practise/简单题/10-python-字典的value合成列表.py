#【字典】给定字典 {'a': [1,2], 'b': [3,4]}，将所有 value 的列表合并为一个大列表 [1,2,3,4]。
#定义一个变量存储字典
dic1 = {'a': [1,2], 'b': [3,4]}
# #定义一个空列表
# ls1 =[]
# #循环遍历对应的value值
# for value in dic1.values():
#     #遍历value值取出每个值
#     for i in value:
#         ls1.append(i)
# #打印结果
# print(ls1)

#列表生成式子
ls1 = [ i for value in dic1.values() for i in value]
print(ls1)