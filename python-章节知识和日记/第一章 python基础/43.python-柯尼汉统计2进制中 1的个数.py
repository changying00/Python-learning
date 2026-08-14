"""
对于一个二进制数 n = 12，其二进制是 1100：
n & (n - 1) 操作将 1100 变成 1000，去除最低的 1。
再进行一次操作，1000 & 0111 = 0000，去除第二个 1。
因此，我们执行了两次操作，所以 n 中有两个 1。

"""
# 从 键盘输入任意一个正整数 
number = int(input("请输入一个正整数"))

print(bin(number))

# 定义一个变量用来存储最终的个数 
count = 0 

# 循环 计算 1 的个数 
while number > 0:
    # 将 number 和 number -1 进行位与运算
    number = number & (number - 1) 
    count += 1

print(count)
