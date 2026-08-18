"""
编写一个程序，要求用户输入一个数字，然后计算该数字的平方根。捕获 ValueError 和 ArithmeticError 异常，并分别打印适当的消息。
"""
import sys
try:
    num = int(input("请输入一个数字(计算平方根):"))
    print(f"{num ** 0.5}")
except ValueError as e:
    print("你输入的数字值不对",str(e))

except ArithmeticError as e:
    print("算术错误",str(sys.exception()))