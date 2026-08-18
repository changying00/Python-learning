"""
创建一个包含数字的列表，尝试访问列表中索引为 "abc" 的元素。捕获 TypeError 异常，并打印一条适当的消息。
"""
try:
    ls = [1,2,3,4,121,777,'abc']
    print(ls["abc"])
except TypeError as e:
    print("索引类型错误",str(e))