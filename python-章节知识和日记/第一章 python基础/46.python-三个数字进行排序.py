"""
从键盘输入 3个数字、并将 三个数字 按照 从大到小的顺序输出 
"""

# 从键盘输入 三个数字 
a = int(input("请输入一个整数"))
b = int(input("请输入一个整数"))
c = int(input("请输入一个整数"))

if a < b:
    a, b = b, a 

if a < c:
    a, c = c, a 

if b < c:
    b, c = c, b

print(a, b, c)