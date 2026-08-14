"""
质数(素数):  一个数字 只能被 1 和它 本身整除 的数  

例如 2,  3, 5, 7, 11, 13, 17, 23, 31, 37, 41, 43, 47, ....


在 python 语言中， while 循环它的完整语法是 

while condition:
    pass

else:
    pass


在 上述 语法中， 当 condition 条件不成立的时候 会执行 else 中的 代码

else 结构 和 break 永远 存在 互斥效果 、 走 break 一定不会执行 else, 走 else 一定不会走 break !!!

"""
# 从键盘输入一个 正整数 
number = int(input("请输入一个正整数\n"))

# 定义一个变量 从  2开始 、到 这个数字的 算术平方根 为止 
x = 2

while x <= number ** 0.5:
    # 判断 x 是否是 number 的因子
    if number % x == 0:
        # 只能说明它一定不是素数 
        print(number, "不是素数")
        # 如果 发现该数字是 合数、则 不需要再进行判断
        break
    # 对 计数器进行 自增 
    x += 1
else:
    # 循环结束后 才能确定 number 是不是素数 
    print(number, "是素数")