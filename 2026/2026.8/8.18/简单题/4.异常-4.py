"""
创建一个包含字符串的列表，尝试将列表中的每个元素转换为整数。捕获 ValueError 异常，并打印一条包含有关错误的消息。
"""
try:
    ls = ['1','2','332','DGX']
    for x in ls:
        x = int(x)
except ValueError as e:
    print("列表中的值错误,不能转成整数",e.args[0])