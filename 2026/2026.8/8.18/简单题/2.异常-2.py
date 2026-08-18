"""
创建一个包含数字的列表，尝试访问列表中索引为 10 的元素。捕获 IndexError 异常，并打印一条适当的消息。
"""
try:
    ls =[1,2,3,4,5,6,7,8]
    index = int(input("请输入索引值:"))
    print(ls[index])
except IndexError as e:
    print("索引超出范围",str(e))