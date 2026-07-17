# 输入一个整数a
a = int(input("请输入一个整数: "))

# 处理负数
if a < 0:
   a = -a

# 把a直接整除求商，赋值给b
b = a //100

# 输出b
print(b)