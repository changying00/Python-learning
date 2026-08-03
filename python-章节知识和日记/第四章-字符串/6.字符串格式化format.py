"""
format(*args, **kwargs)

格式化语法:

    { [index|name]: [填充的单字符] [对齐方式] [填充的宽度] [数字分隔符 , ] [.精度] [类型] }
        < :  左对齐 
        > :  右对齐
        ^ :  居中对齐 
"""
a = 3
b = 4

print("{} + {} = {}".format(a, b, a + b))
print("{1} + {0} = {2}".format(a, b, a + b))
print("{x} + {y} = {z}".format(x=a, y=b, z=a+b))
print("{0} + {x} = {1}".format(a, a+b, x=b))

# 定义一个 数字，用来表示 会员卡 卡号、卡号 为 8 位数
card = 35465

# 输出 会员卡的卡号 
print("我的会员卡卡号是 No.{:0>8}".format(card))

# 定义一个 人的名字 和 年龄 并输出 
name = "张三"
age = 20

print("我的名字叫 {name:*^4}, 今年 {age}岁".format(name=name, age=age))

number = 435478476
print("我的银行余额为{0:,}, 该数字的 八进制是 {0:o}、十六进制是{0:x}".format(number))

# 定义一个圆周率
pi = 3.1415926
print("圆周率为 {x}, 通常使用的值为 {x:.2f}".format(x=pi))

company = "奇酷信息科技有限公司"

print("公司的名字为{0}, 简称{0:.2s}".format(company))

