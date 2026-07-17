"""
【列表】编写一段程序使用循环查找一个数字列表中的最大值和最小值

"""
#定义一个列表
lis_num = [155,32,33,112,34,56,43,23]
#定义一个for循环遍历列表数据
# 定义一个变量max_num,存储最大值，假如首先赋值为列表的第一个数字
# max_num = lis_num[0]
# 定义一个变量min_num,存储最小值，假如首先赋值为列表的第一个数字
# min_num = lis_num[0]
max_num = min_num = lis_num[0]
# for i in range(len(lis_num)):
#     # 判断遍历的数据根max_num对比
#     if lis_num[i] >= max_num:
#         #如果大于max_num的值，则把lis_num[i]的值赋给max_num
#         max_num = lis_num[i]
#     if lis_num[i] <= min_num:
#         # 如果小于min_num的值，则把lis_num[i]的值赋给min_num
#         min_num = lis_num[i]
# #循环遍历完成，输出最小值和最大值
# print("最小值为:",min_num)
# print("最大值为:",max_num)
#改进
for  i in lis_num[1:]:
    if max_num < i:
        max_num = i
    if min_num > i:
        min_num = i
print(max_num,min_num)