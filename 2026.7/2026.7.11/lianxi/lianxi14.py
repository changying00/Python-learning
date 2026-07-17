"""

【循环题】编写一段程序、使用循环计算一个数字的16进制，允许使用字符串拼接

"""

# 定义一个num,接收用户输入的数字

num = int(input("请你输入一个数字:"))
# 存放最终的十六进制字符串
binary = ""
while  True  :
# 取最低4位
    x  = num & 15
# 将得到的余数转换为对应的十六进制字符
    if x == 10:
        binary = "A" + binary
    elif x == 11:
        binary = "B" + binary
    elif x == 12:
        binary = "C" + binary
    elif x == 13:
        binary = "D" + binary
    elif x == 14:
        binary = "E" + binary
    elif x == 15:
        binary = "F" + binary
    else:
        binary = str(x) + binary
    # 右移4位，相当于去掉最低4位
    num = num >> 4
    if num == 0:
# break 可以强制结束循环
       break
# 整个循环结束后、输出 二进制 
print("0x" + binary)

