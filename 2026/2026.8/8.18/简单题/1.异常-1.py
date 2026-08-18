"""编写一个程序，要求用户输入一个数字，然后将其转换为整数。如果用户输入的不是数字，捕获异常并打印一条错误消息。"""

try:
    num = int(input("请输入一个数字:"))
    print(num)
except ValueError:
    print("你输入的不是数字，请重新输入")