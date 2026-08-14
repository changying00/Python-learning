"""
流程控制 - 判断 - 基本使用方式 

单分支条件判断语法：

if condition:
    pass


if : 编写 判断的 关键字 、代表 如果 

condition : 用来定义 执行任务的 条件 

pass :  此时 编写满足条件 执行的任务、 pass 是一个关键字 、在 python 中 是一个占位符，用来保证 语法的完整性



双分支条件判断 语法:

if condition:
    pass 
else:
    pass 


else: 当 if 条件不成立的时候 会执行的代码 

"""

# 从键盘输入一个正数 
n = int(input("请输入一个正数"))

# 判断该整数是否是奇数、如果是、则输出 奇数、 
if n & 1:
    print("奇数")
else:
    print("偶数")
