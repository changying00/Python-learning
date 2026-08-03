# #【字典】给定字典 {'x': [1,2], 'y': [3,4]}，合并所有列表并求和（结果是 10）。
# dic = {'x': [1,2], 'y': [3,4]}
# #取出键"x"对应的列表
# ls = dic.get('x')
# #取出键“y"对应的列表
# ls1 =dic.get('y')
# #对列表进行相加赋值给ls2
# ls2 = ls + ls1
# #print(ls2)
# sum1 = 0
# #for循环遍历值相加
# for i  in ls2:
#     #传入的值每次相加
#     sum1 += i
# #输出打印结果
# print(sum1)

#列表推导式
dic = {'x':[1,2], 'y':[3,4]}
result = sum(
    [num for value in dic.values() for num in value]
)
print(result)