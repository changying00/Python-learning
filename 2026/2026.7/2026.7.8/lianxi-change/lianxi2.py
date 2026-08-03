"""
【运算符】在一个大的笼子中，有鸡和兔若干只，
从上看 有 35个头， 从下看 有94只脚。
 问 鸡和兔各有多少只


"""
# 定义一个变量、存储动物总个数
animal_count = 35

# 定义一个变量、存储动物所有脚的数量

# 计算 兔子的个数(假设所有动物均为2条腿),多余的腿为兔子的个数
animal_leg = 94

# 计算 兔子的个数
rabbit_count =(animal_leg - animal_count * 2 )//2

#计算鸡的数量

rest_count = animal_count - rabbit_count

print("兔子的数量",rabbit_count,"鸡的数量",rest_count)