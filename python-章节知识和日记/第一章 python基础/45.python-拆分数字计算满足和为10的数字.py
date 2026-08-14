"""
统计 1~1000 中，数字之和等于 10 的所有数 。例：28 = 2 + 8 = 10，55 = 5 + 5 = 10


求 5!

求 5! + 4! + ... + 1 的 和 

"""

# 使用 for 循环 来遍历 10 ~ 1000 以内的所有数字 

# for number in range(10, 1000):
#     # 定义一个变量、用来存储当前数字 number 它的每一位数字的和 
#     s = 0
#     # 定义一个变量、存储 number 的初始值 
#     _number = number  
#     # 使用 while 循环、获取 数字上的每一位数字 
#     while _number > 0:
#         x = _number % 10 
#         # 将每一个数字 累加求和
#         s += x 
#         _number //= 10

#     # 循环结束、判断 s 的和 是否等于 10 
#     if s == 10:
#         print(number)


# 定义一个变量、存储最终结果 
#
s, ret = 1, 0
# 从 5 遍历 到 1 
for n in range(1, 6):
    s *= n 
    ret += s 

print(ret)

# ret = 0

# for n in range(5, 0, -1):
#     s = 1
#     # 求 n 的阶乘 
#     for x in range(1, n+1):
#         s *= x 

#     ret += s 

# print(ret)