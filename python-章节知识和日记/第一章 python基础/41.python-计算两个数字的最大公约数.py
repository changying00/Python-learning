"""
计算 2个数字的最大公约数 

    1.  断除法 将 所有的因子 相乘 

    2.  辗转相减法 、直到 2个数字相同、差为 0

    3.  辗转相除求余 、 直到 余数为 0

"""
a = int(input("请输入一个正整数\n"))
b = int(input("请输入一个正整数\n"))


while True:
    # 比较 a 和 b 的大小 规定 a >= b 
    if a < b:
        a, b = b, a 
    # 将 a  和 b 做 求余运算 
    a = a % b 
    if a == 0:
        break 

print(b)


# while a != b:
#     # 比较 a 和 b 的大小、 规定 a >= b
#     if a < b:
#         # 交换 2个数字
#         a, b = b, a 
#     # 将 a 和 b 做减法运算 
#     a = a - b

# print(a)

# x = 2 

# # 定义一个变量、存储所有的因子乘积
# z = 1

# while x <= a and x <= b: 

#     if a % x == 0 and b % x == 0:
#         z = z * x 
#         # 将 a 和 b 缩小 x 倍
#         a, b = a // x , b //x 
#         continue
#     x = x + 1

# print(z)






