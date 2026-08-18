"""
编写一个程序，要求用户输入两个数字，并尝试将它们相除。捕获 ZeroDivisionError 异常，
如果发生异常，则打印一条提醒用户不能除以零的消息。
"""
try:
    num1 = int(input("请输入第一个数。被除数:"))
    num2 = int(input("请输入第二个数，除数:"))
    result = num1 / num2
except ZeroDivisionError as e:
    print("不能除以零",e.args[0])