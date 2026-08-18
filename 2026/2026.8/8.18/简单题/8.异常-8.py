"""
创建一个包含整数的列表，尝试计算列表中每个元素的倒数。捕获 ZeroDivisionError 异常，并打印一条提醒用户不能除以零的消息。
"""

try:
    ls = [11,52,43,43,152,0]
    for x in ls:
        print(f'{1/x}')
except ZeroDivisionError as e:
    print("除数不能为零",str(e))