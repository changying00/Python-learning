"""
while 循环 处理 循环次数不确定的任务 

#  从键盘输入一个正整数 、 并输出 该数字的 所有 因子 

#  使用 循环 计算一个 正整数的 二进制 、不允许 bin 函数 


在 循环次数不确定的任务中， 可以使用 break 关键字 强制 终止循环 


"""

number = int(input("请输入一个正整数"))

# 定义一个变量、用来存储最终的二进制 
binary = ""

# 定义一个 while 循环 处理任务 
while True:
    # 在循环体中 执行重复的任务 、不断的 整除 2 求余、求商 
    # 定义一个变量、用来存储 余数 
    x = number & 1
    # 将 得到的余数 和 binary 进行拼接、且放在 字符串的最前面
    binary = str(x) + binary
    # 将 number 整除 2 求商、并赋值给 number 、进行下一次的重复任务 
    number = number >> 1
    # 添加一个判断条件、当 满足条件、退出循环
    if number == 0:
        # break 可以强制结束循环
        break
        
# 整个循环结束后、输出 二进制 
print("0b" + binary)