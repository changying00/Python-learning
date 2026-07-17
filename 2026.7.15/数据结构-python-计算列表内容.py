"""

【列表】有一个列表，数据内容为 [1, 5, 10, 10, 5, 1] ,
 编写一个算法、能够将数组中的值通过计算得到 161051。
"""
#第一次理解这个题，有点浅，没读懂
# #定义一个列表
# ls = [1,5,10,10,5,1]
# #定义一个变量接收数据
# num = 0
# #定义一个空字符串
# num1 = ""
# #遍历ls列表中前三项数据
# for i in range(3):
#     #把ls列表前三项的数加起来
#     num += ls[i]
# for j in range(3,6):
#     #把后三项当字符串加起来
#     num1 += str(ls[j])
# #字符串相加
# num2 = str(num) + str(num1)
# #打印结果
# print(num2)

# ls = [1,5,10,10,5,1]
# #按照 进制转换的方式 将其转成10进制
# #定义一个变量number 用来存储最后的结果
# number = 0
# #倒叙遍历列表 、将每一位 和10 的幂次方做运算 累加求和
# for i in range(len(ls)-1,-1,-1): #因为要取到0 所以取到end = -1
#     #获取 幂次方 幂值
#     pow = len(ls) -1 -i
#     number +=  ls[i] * 10 **pow
# print(number)

#二进制转 10进制
num = "1011"
#定义一个变量number，存储和
number = 0
#遍历
for i in range(len(num)-1,-1,-1):
    pow = len(num) -1 -i
    number += int(num[i]) * 2 **pow
print(number)