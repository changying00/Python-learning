"""【循环】编写一个程序，使用while循环计算并打印出一个给定整数的所有因数。"""
# 定义一个num，接收用户给的整数
num = int(input("请输入一个给定整数:"))
# 定义一个变量 count 接收所有因数
count = str(1)
x = 1
while x < num:
    if (num % x) == 0:
       count1 = num / x
       count  = count +","+ str(count1)
    x += 1
print(count)