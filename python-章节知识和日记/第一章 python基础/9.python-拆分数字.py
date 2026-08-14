# coding=gbk

"""
拆分数字 

"""
number = int(input("请输入一个要拆分的正整数"))

# 获取 个位数 
x = number % 10

# 获取 十位数 (将要求的位数做成 最低位)
# y = number // 10 % 10
# 将要求的位数 做成 最高位 
y = number % 100 // 10

# 获取 百位数
# z = number // 100 % 10
z = number % 1000 // 100

print(x, y, z)
