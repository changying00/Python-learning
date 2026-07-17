"""

【循环】编写一个程序，使用while循环判断一个给定的整数是否为质数（只能被1和自身整除）。
有时候可以反方向想一想
"""
num = int (input("请你输入一个整数:"))
x = 2
while x < num:
    if num % x == 0:
        print("该数不是质数")
        break  
    x += 1
else:
    print("该数是质数")    
       