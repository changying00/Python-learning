"""
1.  计算 4个字节 除符号位 最高位 是 0 还是 1

2.  鸡兔同笼 

3.  拆分数字、并重新组装数字 

"""

number = int(input("请输入一个长度为3的正整数"))

# 获取个位数 
a = number % 10
# 获取十位数
b = number // 10 % 10
# 获取百位数
c = number // 100

# 重新组装数字
new_number = a * 100 + b * 10 + c 
# 输出这个数字
print(number, "数字反转后是", end="")
print(new_number)




# 定义一个变量、存储动物总个数 
animal_count = 35
# 定义一个变量、存储动物所有脚数量
animal_foot_count = 94

# 计算 兔子的个数 (假设所有动物均有2条腿)、多余的腿 一定是 兔子的2条腿
rabbit_count = (animal_foot_count - animal_count * 2) // 2

# 计算 鸡的数量 
rest_count = animal_count - rabbit_count

print("兔子的数量:", rabbit_count, "鸡的数量:", rest_count)



# 定义一个数字
number = 0xf3c1f3c1

print(bin(number))

# 使用 & 运算 计算 第 31位是 1 还是 0 
ret = number & (2 ** (4 * 8 - 1 - 1))

if ret > 0:
    print("1")
else:
    print("0")


